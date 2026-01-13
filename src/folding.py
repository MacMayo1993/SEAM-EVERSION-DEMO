import numpy as np
from .constants import C_OUT, C_IN

def get_folding_geometry(fold_progress, inverted=False):
    """
    Net ↔ Cube folding.
    fold_progress: 0 (flat net) → 1 (folded cube)
    inverted: True for post-eversion colors
    """
    s = 1.0  # size
    angle = fold_progress * (np.pi / 2)
    c_main = C_OUT if not inverted else C_IN

    faces = []

    # Helper square
    base_sq = np.array([
        [-s, -s, 0],
        [ s, -s, 0],
        [ s,  s, 0],
        [-s,  s, 0]
    ]) / 2

    # Bottom (fixed)
    faces.append((base_sq.copy(), c_main))

    # Rotation matrices
    def rotate_x(v, a):
        c, s = np.cos(a), np.sin(a)
        R = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
        return np.dot(v, R.T)

    def rotate_y(v, a):
        c, s = np.cos(a), np.sin(a)
        R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        return np.dot(v, R.T)

    # Simplified interpolation for sides (flat → cube positions)
    # Left
    pts_flat = base_sq + [-1, 0, 0]
    pts_cube = rotate_y(base_sq, -np.pi/2) + [-0.5, 0, 0.5]
    pts = pts_flat * (1 - fold_progress) + pts_cube * fold_progress
    faces.append((pts, c_main))

    # Right
    pts_flat = base_sq + [1, 0, 0]
    pts_cube = rotate_y(base_sq, np.pi/2) + [0.5, 0, 0.5]
    pts = pts_flat * (1 - fold_progress) + pts_cube * fold_progress
    faces.append((pts, c_main))

    # Back
    pts_flat = base_sq + [0, 1, 0]
    pts_cube = rotate_x(base_sq, -np.pi/2) + [0, 0.5, 0.5]
    pts = pts_flat * (1 - fold_progress) + pts_cube * fold_progress
    faces.append((pts, c_main))

    # Front
    pts_flat = base_sq + [0, -1, 0]
    pts_cube = rotate_x(base_sq, np.pi/2) + [0, -0.5, 0.5]
    pts = pts_flat * (1 - fold_progress) + pts_cube * fold_progress
    faces.append((pts, c_main))

    # Top
    pts_flat = base_sq + [0, 2, 0]
    pts_cube = base_sq + [0, 0, 1.0]
    pts = pts_flat * (1 - fold_progress) + pts_cube * fold_progress
    faces.append((pts, c_main))

    return faces
