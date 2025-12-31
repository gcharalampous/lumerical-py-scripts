#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='2.0'   # AC sweep version
# ---------------------------------------------------------------------------

import os
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from pathlib import Path

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
from DEVICE.disk_modulator.analytical_calculations.capacitance_analytical import capDCanalytical
from DEVICE.disk_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.disk_modulator.user_inputs.user_materials import *  
from DEVICE.disk_modulator.user_inputs.user_sweep_parameters import *
from DEVICE.disk_modulator.waveguide_render import waveguide_draw
from DEVICE.disk_modulator.charge_region import add_charge_region
from config import *

epsilon0 = 8.854187817620e-12               # [F/m]
epsilon_s = 11.8                            # Si Relative Dielectric constant
q = 1.60217646e-19                          # Electronic charge [Coulombs]

# -------- AC helper (robust to missing user params) --------
def _get_ac_params():
    # If you already define these in user_sweep_parameters, they will be present.
    # Otherwise we provide safe defaults.
    f_start = globals().get("ac_start_frequency", 1e6)          # 1 MHz
    f_stop  = globals().get("ac_stop_frequency", 5e10)          # 50 GHz
    ppd     = globals().get("ac_points_per_decade", 50)
    bias_list = globals().get("ac_bias_list", [0.0])            # list of DC biases (V)
    return f_start, f_stop, ppd, bias_list

def setup_dc_and_ac(device, v_bias, f_start, f_stop, points_per_decade):
    # --- Set DC operating point on contacts ---
    device.switchtolayout()
    device.setnamed("CHARGE::boundary conditions::anode", "voltage", v_bias)  # 
    
    
    # --- Configure AC sweep in CHARGE ---
    device.setnamed("CHARGE", "norm length", device_length)
    device.setnamed("CHARGE", "solver mode", "ssac")
    device.setnamed("CHARGE", "solver type", "newton")
    
    device.setnamed("CHARGE", "frequency spacing", "log") 
    device.setnamed("CHARGE", "log start frequency", float(f_start))
    device.setnamed("CHARGE", "log stop frequency", float(f_stop))
    device.setnamed("CHARGE", "log stop frequency", float(f_stop))
    device.setnamed("CHARGE", "num frequency points per dec", int(ac_points_per_decade))

    # --- Small-signal excitation: drive anode with 1 V ---
    device.setnamed("CHARGE::boundary conditions::anode", "apply ac small signal", "all")
    # device.setnamed("anode", "ac phase", 0.0)
    # device.setnamed("cathode", "ac amplitude", 0.0)

def run_ac(device):
    # Runs DC first, then AC linearized about the DC point
    device.run()

    # --- Read AC results ---
    # Frequency vector
    f = device.getdata("CHARGE","ac_anode","f")  # Hz
    
    # Complex impedance looking into "anode"
    dI = device.getdata("CHARGE","ac_anode","dI")  # A (complex)
    
    # Complex impedance (use '-' only if needed for your port orientation)
    Z = perturbation_amplitude / dI  # V / A = Ohms (complex)

    # Flatten
    f = np.squeeze(f)
    Z = np.squeeze(Z)

    # Drop any zero frequency to avoid division by zero in C extraction
    valid = f > 0
    f = f[valid]; Z = Z[valid]

    w = 2*np.pi*f
    Rs_series = np.real(Z)                   # Ω
    Xs = np.imag(Z)                          # Ω (should be negative if capacitive)
    Cs_series = np.where(Xs < 0, -1/(w*Xs), np.nan)   # F
    
    



    # # Admittance and parallel RC
    # Y = 1.0 / Z
    # G = np.real(Y)
    # B = np.imag(Y)

    # # Guard against numerical negatives/zeros in G
    # eps = 1e-15
    # G = np.where(G > eps, G, np.nan)

    # Rp = 1.0 / G                         # parallel resistance (Ohms)
    # Ceff = B / (2.0 * np.pi * f)         # effective (parallel) capacitance (F)

    return f, Z, Rs_series, Cs_series

def plot_and_save_ac(f, Z, Ceff, v_bias, out_dir, dpi):
    os.makedirs(out_dir, exist_ok=True)
    
    # Ensure arrays are 1D
    f = np.squeeze(f)
    Z = np.squeeze(Z)
    Ceff = np.squeeze(Ceff)

    # |Z(f)|
    plt.figure(figsize=(512/dpi, 256/dpi), dpi=dpi)
    plt.loglog(f, np.abs(Z), '-')
    plt.grid(True, which='both')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|Z| (Ω)")
    plt.title(f"Impedance vs Frequency @ V_anode = {v_bias:.3f} V")
    file_imp = os.path.join(str(out_dir), f"Impedance_AC_{v_bias:+.3f}V.png")
    plt.tight_layout()
    plt.savefig(file_imp)

    # Ceff(f)
    plt.figure(figsize=(512/dpi, 256/dpi), dpi=dpi)
    plt.loglog(f, Ceff*1e15, '-')
    plt.grid(True, which='both')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Capacitance (fF)")
    plt.title(f"Ceff vs Frequency @ V_anode = {v_bias:.3f} V")
    file_cap = os.path.join(str(out_dir), f"Capacitance_AC_{v_bias:+.3f}V.png")
    plt.tight_layout()
    plt.savefig(file_cap)
    
    # R
    plt.figure(figsize=(512/dpi, 256/dpi), dpi=dpi)
    plt.loglog(f, R, '-')
    plt.grid(True, which='both')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Resistance (Ω)")
    plt.title(f"Resistance vs Frequency @ V_anode = {v_bias:.3f} V")
    file_res = os.path.join(str(out_dir), f"Resistance_AC_{v_bias:+.3f}V.png")
    plt.tight_layout()
    plt.savefig(file_res)

    return file_imp, file_cap


def write_s1p_from_impedance(f, Z, filename, z0=50.0, unit="Hz", fmt="RI"):
    """
    Write a 1-port Touchstone (.s1p) file from frequency and complex impedance data.
    - f: array-like frequencies (use units consistent with `unit`)
    - Z: array-like complex impedance
    - filename: output .s1p path
    - z0: reference impedance in the Touchstone header
    - unit: {"Hz","kHz","MHz","GHz"} (label only; values are not auto-rescaled)
    - fmt:  {"RI","MA"} (Real/Imag or Mag/Angle(deg))
    """
    unit = unit.upper()
    if unit not in {"HZ", "KHZ", "MHZ", "GHZ"}:
        raise ValueError("unit must be one of {'Hz','kHz','MHz','GHz'}")

    fmt = fmt.upper()
    if fmt not in {"RI", "MA"}:
        raise ValueError("fmt must be 'RI' or 'MA'")

    f = np.asarray(f, dtype=float)
    Z = np.asarray(Z, dtype=complex)
    print(Z)
    if f.shape != Z.shape:
        raise ValueError("f and Z must have the same shape")

    mask = np.isfinite(f) & np.isfinite(Z.real) & np.isfinite(Z.imag) & (f > 0)
    f = f[mask]; Z = Z[mask]
    order = np.argsort(f)
    f = f[order]; Z = Z[order]

    if f.size == 0:
        raise ValueError("No valid data points to write.")

    # Z -> S11
    S11 = (Z - z0) / (Z + z0)

    header = f"# {unit} S {fmt} R {z0:g}\n"
    filename = Path(filename)
    with filename.open("w", encoding="utf-8") as fh:
        fh.write(header)
        if fmt == "RI":
            for fi, s in zip(f, S11):
                fh.write(f"{fi:.9e} {s.real:.9e} {s.imag:.9e}\n")
        else:
            mag = np.abs(S11)
            ang = np.degrees(np.angle(S11))
            for fi, m, a in zip(f, mag, ang):
                fh.write(f"{fi:.9e} {m:.9e} {a:.9e}\n")
    return str(filename.resolve())

if __name__ == "__main__":
    with lumapi.DEVICE() as device:
        # Build geometry & simulation region
        device.redrawoff()
        waveguide_draw(device)
        add_charge_region(device)

        # Save model once
        device.save(PIN_MODULATOR_DIRECTORY_WRITE_FILE + "\\pin_waveguide_simulation.ldev")

        # --- AC sweep(s) ---
        f_start, f_stop, ppd, bias_list = _get_ac_params()

        saved_images = []
        s1p_path = None  # Initialize to avoid unbound error
        for v_bias in bias_list:
            setup_dc_and_ac(device, v_bias, f_start, f_stop, ppd)
            f, Z, R, Ceff = run_ac(device)

            # Persist numeric outputs (per-bias)
            npz_path = os.path.join(str(PIN_MODULATOR_DIRECTORY_WRITE[1]),
                                    f"ac_sweep_{v_bias:+.3f}V.npz")
            np.savez(npz_path, frequency=f, Z=Z, Ceff=Ceff)

            s1p_file = os.path.join(str(PIN_MODULATOR_DIRECTORY_WRITE[1]),
                                    f"ac_sweep_{v_bias:+.3f}V.s1p")
            s1p_path = write_s1p_from_impedance(f, Z, s1p_file, z0=50.0, unit="Hz", fmt="RI")


            # Optional: MATLAB file
            try:
                device.matlabsave(os.path.join(str(PIN_MODULATOR_DIRECTORY_WRITE[1]),
                                  f"ac_sweep_{v_bias:+.3f}V.mat"), "f", "Z", "Ceff")
            except Exception:
                # If MATLAB saving isn’t available in this context, ignore
                pass

            # Plots
            imp_png, cap_png = plot_and_save_ac(
                f, R, Ceff, v_bias,
                out_dir=str(PIN_MODULATOR_DIRECTORY_WRITE[1]),
                dpi=my_dpi
            )
            saved_images.extend([imp_png, cap_png])

        device.redrawon()

        # Console summary
        print("AC sweep complete.")
        print(f"Biases swept (V): {bias_list}")
        print(f"Frequency range: {f_start:.3g} Hz → {f_stop:.3g} Hz (log, {ppd} pts/dec)")
        print("Saved:", *saved_images, sep="\n - ")
        
        
        print("Wrote:", s1p_path)
