# Techniques de Haute Tension — LaTeX Package
## How to Compile

### Requirements
Install these packages first:
```
pip install matplotlib numpy
```

For LaTeX, you need a full TeX distribution:
- **Windows**: MiKTeX (https://miktex.org) or TeX Live
- **Linux/Mac**: TeX Live (`sudo apt install texlive-full` or `brew install texlive`)
- **Online**: Upload to Overleaf (https://overleaf.com) — easiest option!

### LaTeX packages needed (auto-installed by MiKTeX/TeX Live):
- babel (french), lmodern, geometry, xcolor (dvipsnames)
- tikz, pgfplots, tcolorbox, booktabs, tabularx
- titlesec, tocloft, fancyhdr, hyperref, siunitx
- amsmath, microtype, enumitem, caption, wrapfig

---

### Step 1 — Generate figures
```bash
python generate_figures.py
```
This creates a `figures/` folder with 11 PNG files.

### Step 2 — Compile LaTeX
```bash
pdflatex main.tex
pdflatex main.tex    # run twice for correct TOC
```
Or with latexmk (recommended):
```bash
latexmk -pdf main.tex
```

### Step 3 — Output
`main.pdf` — your complete document!

---

### Using Overleaf (Easiest)
1. Go to https://overleaf.com
2. New Project → Upload Project
3. Zip this entire folder and upload
4. Click Compile
5. Download PDF

---

### Files in this package:
- `main.tex`          — Main LaTeX document (~900 lines)
- `generate_figures.py` — Python script to generate all figures
- `figures/`          — Generated PNG figures (after running the script)
- `README.md`         — This file

---

### Figures generated:
| File | Description |
|------|-------------|
| fig_electric_field.png | Champ uniforme vs non-uniforme |
| fig_paschen.png | Courbe de Paschen complète |
| fig_corona.png | Effet corona (fond sombre) |
| fig_impulse.png | Ondes 1.2/50µs et 250/2500µs |
| fig_marx.png | Générateur de Marx 4 étages |
| fig_insulation_coord.png | Niveaux de coordination |
| fig_coaxial_field.png | Champ dans câble coaxial |
| fig_partial_discharge.png | Modèle décharges partielles |
| fig_sphere_gap.png | Éclateur à sphères |
| fig_townsend.png | Avalanche de Townsend |
| fig_voltage_divider.png | Diviseurs R, C, RC |
