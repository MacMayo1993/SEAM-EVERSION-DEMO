# SEAM VIZ Eversion Demo

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

## Quick Start with GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/MacMayo1993/SEAM-EVERSION-DEMO)

The fastest way to run this demo is with GitHub Codespaces:

1. Click the badge above or the "Code" button on GitHub
2. Select "Create codespace on main"
3. Wait for the environment to set up (dependencies install automatically)
4. Run `python src/main.py` or open the Jupyter notebook

Everything is pre-configured and ready to go!

## Installation

```bash
git clone https://github.com/MacMayo1993/SEAM-EVERSION-DEMO.git
cd SEAM-EVERSION-DEMO
pip install -r Requirements.txt
```

## Run the animation (static GIF)

```bash
python src/main.py
```

Outputs `output/full_cycle_eversion.gif`

## Interactive version (Jupyter)

Open Jupyter:

```bash
jupyter notebook notebooks/interactive_demo.ipynb
```

Use sliders to control t (time through manifold) and k* (decay scale).

## License

MIT License

## Related Work

Companion demo for the SEAM VIZ paper on regime-switching visualization via information geometry and ℝP².
