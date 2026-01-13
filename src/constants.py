import numpy as np

# ==========================================
# CONSTANTS & CONFIG
# ==========================================
K_STAR = 1.0 / (2.0 * np.log(2.0))          # ≈ 0.721347
Z_BELT = 0.25

# Color Palette (Blue/Green for contrast)
C_OUT = np.array([0.1, 0.6, 1.0])           # Blue (Outside/Forward)
C_IN  = np.array([0.2, 0.8, 0.2])           # Green (Inside/Backward)

# Animation settings
N_POINTS = 30                               # Resolution for meshgrid
OUTPUT_DIR = "output"
