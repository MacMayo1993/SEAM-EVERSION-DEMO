import numpy as np
from .constants import K_STAR, Z_BELT, C_OUT, C_IN, N_POINTS

def z_mayo(t):
    """Exponential information decay from the seam."""
    return np.exp(-np.abs(t) / K_STAR)

def get_superellipsoid_radius(theta, phi, n):
    """Superellipsoid radius (n=2 → sphere, n→∞ → cube)."""
    sin_p, cos_p = np.sin(phi), np.cos(phi)
    sin_t, cos_t = np.sin(theta), np.cos(theta)

    term_x = np.abs(sin_p * cos_t)**n
    term_y = np.abs(sin_p * sin_t)**n
    term_z = np.abs(cos_p)**n

    return np.power(term_x + term_y + term_z, -1.0/n)

def get_continuous_geometry(morph_factor, t_mayo):
    """
    Generate sphere/cube morph + Mayo/Thurston eversion.

    morph_factor: 0 (cube-like) → 1 (sphere)
    t_mayo: drives eversion progress
    """
    theta = np.linspace(0, 2*np.pi, N_POINTS)
    phi = np.linspace(0, np.pi, N_POINTS)
    THETA, PHI = np.meshgrid(theta, phi)

    # Shape exponent: 10 (cube-ish) → 2 (sphere)
    n = 10.0 - 8.0 * morph_factor

    # Mayo height & eversion progress
    z_h = z_mayo(t_mayo)
    ever_prog = 0.5 * (1 + np.tanh(t_mayo / K_STAR))

    # Corrugations (ripple) strongest near belt
    freq = 6 * (1 - z_h) if z_h < 1 else 0
    amp = 0.15 * (1 - abs(z_h - Z_BELT)/Z_BELT) if z_h < 0.5 else 0
    amp = max(0, amp)
    ripple = amp * np.sin(freq * THETA) * np.sin(freq * PHI)

    # Eversion twist
    flip_angle = np.pi * ever_prog
    phi_new = PHI + flip_angle * np.sin(THETA) * np.sin(PHI)

    # Base radius + ripple
    R_base = get_superellipsoid_radius(THETA, phi_new, n)
    R = R_base * (1.0 + ripple)

    X = R * np.sin(phi_new) * np.cos(THETA)
    Y = R * np.sin(phi_new) * np.sin(THETA)
    Z = R * np.cos(phi_new)

    # Color: interpolate from inside (green) to outside (blue)
    base_color = C_IN * (1 - ever_prog) + C_OUT * ever_prog
    C = np.tile(base_color, (N_POINTS, N_POINTS, 1))

    return X, Y, Z, C
