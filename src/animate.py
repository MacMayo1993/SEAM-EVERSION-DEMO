import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .constants import N_POINTS, OUTPUT_DIR
from .geometry import get_continuous_geometry
from .folding import get_folding_geometry
import os

def update(frame, ax, n_frames):
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.axis('off')

    # Timeline division (180 frames total example)
    if frame < 30:          # Phase 1: Fold net → cube
        p = frame / 30.0
        faces = get_folding_geometry(p, inverted=False)
        for v, c in faces:
            ax.add_collection3d(Poly3DCollection([v], facecolor=c, edgecolor='k', alpha=0.9))
        status = "Phase 1: Assembly (Net → Cube)"

    elif frame < 60:        # Phase 2: Morph cube → sphere
        p = (frame - 30) / 30.0
        X, Y, Z, C = get_continuous_geometry(p, -3.0)  # Stable t=-3
        ax.plot_surface(X, Y, Z, facecolors=C, shade=True)
        status = "Phase 2: Morph (Cube → Sphere)"

    elif frame < 120:       # Phase 3: Eversion (main event!)
        p_anim = (frame - 60) / 60.0
        t = -3.0 + p_anim * 6.0
        X, Y, Z, C = get_continuous_geometry(1.0, t)  # Full sphere
        ax.plot_surface(X, Y, Z, facecolors=C, shade=True)
        z_val = np.exp(-np.abs(t) / (1/(2*np.log(2))))
        state = "Seam" if abs(t) < 0.2 else ("Belt" if abs(z_val - 0.25) < 0.05 else "Eversion")
        status = f"Phase 3: Eversion (t={t:.1f}, z={z_val:.2f}, {state})"

    elif frame < 150:       # Phase 4: Crystallize inverted sphere → cube
        p = (frame - 120) / 30.0
        X, Y, Z, C = get_continuous_geometry(1.0 - p, 3.0)  # t=3, morph back
        ax.plot_surface(X, Y, Z, facecolors=C, shade=True)
        status = "Phase 4: Crystallization (Inverted)"

    else:                   # Phase 5: Unfold inverted cube → net
        p = (frame - 150) / 30.0
        faces = get_folding_geometry(1.0 - p, inverted=True)
        for v, c in faces:
            ax.add_collection3d(Poly3DCollection([v], facecolor=c, edgecolor='k', alpha=0.9))
        status = "Phase 5: Disassembly (Inverted)"

    ax.set_title(status, fontsize=12, fontweight='bold')

def run_animation(n_frames=180, fps=20, dpi=100):
    print("Starting animation render...")
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    anim = FuncAnimation(fig, update, fargs=(ax, n_frames), frames=n_frames, interval=50)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{OUTPUT_DIR}/full_cycle_eversion.gif"
    print(f"Saving to {filename}...")
    anim.save(filename, writer=PillowWriter(fps=fps), dpi=dpi)
    plt.close(fig)
    print("Done!")
