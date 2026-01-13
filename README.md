# SEAM Eversion Demo

Animated proof-of-concept for the regime-switching "flip" in the real projective plane (ℝP²), as visualized in SEAM VIZ.

## What it shows

A full cycle demonstrating smooth orientation swap without discontinuities:

- Phase 1: Flat net folds into a cube (assembly)
- Phase 2: Cube morphs to sphere (smooth manifold)
- Phase 3: Sphere everts inside-out through the Mayo manifold (z(t) exponential decay, corrugations peak at belt z=0.25)
- Phase 4: Inside-out sphere crystallizes back to inverted cube
- Phase 5: Inverted cube unfolds to net (colors swapped = orientation flip)

The eversion phase shows how Regime A smoothly occupies the space of Regime B — no cuts, no singularities, just continuous deformation through non-orientable topology.

This illustrates the core "think through the box, orthogonally" idea: regimes flip by navigating the geometry, not by forcing artificial jumps.

## Installation

```bash
git clone https://github.com/YOURUSERNAME/seam-viz-eversion-demo.git
cd seam-viz-eversion-demo
pip install -r requirements.txt
