"""
Generate all figures for the HV Engineering LaTeX document.
Outputs PNG files into ./figures/ directory.
Run: python generate_figures.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import os

# ─── Setup ───────────────────────────────────────────────────────────────────
FIGDIR = "./figures"
os.makedirs(FIGDIR, exist_ok=True)

# Color palette (matches LaTeX document)
C = {
    'darkblue':   '#0D2B55',
    'midblue':    '#1A4A8A',
    'lightblue':  '#3A7CC1',
    'accent':     '#E8A020',
    'lightgray':  '#F4F6F9',
    'hvred':      '#C0392B',
    'hvgreen':    '#1A7A4A',
    'textdark':   '#1A202C',
    'textmed':    '#4A5568',
    'boxbg':      '#EBF4FF',
}

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': C['lightgray'],
    'axes.facecolor': C['lightgray'],
    'axes.labelcolor': C['textdark'],
    'xtick.color': C['textdark'],
    'ytick.color': C['textdark'],
    'axes.titlecolor': C['darkblue'],
})

def save(fig, name, dpi=180):
    path = os.path.join(FIGDIR, f"{name}.png")
    fig.savefig(path, dpi=dpi, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  Saved: {path}")

# ─────────────────────────────────────────────────────────────────────────────
# FIG 1 — Electric field: uniform vs non-uniform
# ─────────────────────────────────────────────────────────────────────────────
def fig_electric_field():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor(C['lightgray'])

    # --- Left: Parallel plates (uniform) ---
    ax = axes[0]
    ax.set_facecolor('#EFF4FF')
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5.5)

    ax.add_patch(patches.Rectangle((-0.7, -0.6), 0.45, 5.2,
                                    color=C['darkblue'], zorder=3))
    ax.add_patch(patches.Rectangle((4.25, -0.6), 0.45, 5.2,
                                    color=C['hvred'], zorder=3))

    for y in np.linspace(0.2, 4.8, 7):
        ax.annotate('', xy=(4.1, y), xytext=(0.1, y),
                    arrowprops=dict(arrowstyle='->', color=C['lightblue'],
                                   lw=1.8, mutation_scale=18))

    ax.text(-0.5, -0.9, '—', fontsize=22, color=C['darkblue'],
            ha='center', fontweight='bold')
    ax.text(4.5, -0.9, '+', fontsize=22, color=C['hvred'],
            ha='center', fontweight='bold')
    ax.text(2.1, -0.75, 'E = U/d  (uniforme)', fontsize=12,
            ha='center', color=C['midblue'], style='italic')
    ax.set_title('Champ électrique uniforme\n(plaques parallèles)', fontsize=13,
                 color=C['darkblue'], fontweight='bold', pad=10)

    # Dimension arrow
    ax.annotate('', xy=(4.2, -0.6), xytext=(0.0, -0.6),
                arrowprops=dict(arrowstyle='<->', color=C['accent'], lw=2))
    ax.text(2.1, -0.72, '', fontsize=0)  # placeholder
    ax.text(2.1, 5.2, 'd', fontsize=14, color=C['accent'],
            ha='center', style='italic')
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)

    # --- Right: Point charge (non-uniform) ---
    ax2 = axes[1]
    ax2.set_facecolor('#EFF4FF')
    ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3.5)

    # Equipotential circles
    for r, ls in [(0.5,'--'), (1.0,'--'), (1.6,'--'), (2.4,':')]:
        circle = plt.Circle((0,0), r, fill=False,
                              color=C['lightblue'], ls=ls, lw=1.2, alpha=0.8)
        ax2.add_patch(circle)
        ax2.text(r*0.7, r*0.7+0.1, f'V={int(10/r)}', fontsize=7.5,
                 color=C['lightblue'], alpha=0.9)

    # Field lines (arrows)
    for angle in np.linspace(0, 360, 14, endpoint=False):
        rad = np.radians(angle)
        r0, r1 = 0.28, 2.2
        ax2.annotate('', xy=(r1*np.cos(rad), r1*np.sin(rad)),
                     xytext=(r0*np.cos(rad), r0*np.sin(rad)),
                     arrowprops=dict(arrowstyle='->', color=C['hvred'],
                                    lw=1.5, mutation_scale=14, alpha=0.85))

    # Charge
    charge = plt.Circle((0,0), 0.25, color=C['hvred'], zorder=5)
    ax2.add_patch(charge)
    ax2.text(0, 0, '+Q', fontsize=9, ha='center', va='center',
             color='white', fontweight='bold', zorder=6)

    ax2.text(0, -2.8, r'E(r) = Q / (4πε₀r²)  ∝ 1/r²', fontsize=11.5,
             ha='center', color=C['midblue'], style='italic')
    ax2.set_title('Champ non uniforme\n(charge ponctuelle)', fontsize=13,
                  color=C['darkblue'], fontweight='bold', pad=10)
    ax2.text(-2.8, 2.5, 'Équipotentielles', fontsize=9, color=C['lightblue'])
    ax2.text(-2.8, 2.1, '(tirets)', fontsize=8, color=C['lightblue'])
    ax2.text(1.5, -2.5, 'Lignes de champ →', fontsize=9, color=C['hvred'])
    ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values(): sp.set_visible(False)

    fig.suptitle('Distribution du Champ Électrique', fontsize=15,
                 color=C['darkblue'], fontweight='bold', y=1.01)
    fig.tight_layout(pad=2.0)
    save(fig, 'fig_electric_field')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 2 — Paschen curve
# ─────────────────────────────────────────────────────────────────────────────
def fig_paschen():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(C['lightgray'])
    ax.set_facecolor('#F0F4FF')

    # Paschen curve for air
    pd = np.logspace(-0.5, 2.5, 600)
    gamma = 0.01
    with np.errstate(divide='ignore', invalid='ignore'):
        denom = np.log(11.5 * pd) - np.log(np.log(1 + 1/gamma))
        Vb = np.where(denom > 0, 364 * pd / denom, np.nan)

    # Only plot valid region
    mask = (pd > 1) & np.isfinite(Vb) & (Vb > 0) & (Vb < 5000)
    ax.semilogx(pd[mask], Vb[mask], color=C['darkblue'], lw=2.8,
                label='Tension de claquage $V_b$ — Air')

    # Shade under curve
    ax.fill_between(pd[mask], Vb[mask], alpha=0.07, color=C['lightblue'])

    # Minimum
    idx_min = np.argmin(Vb[mask])
    pd_min = pd[mask][idx_min]
    Vb_min = Vb[mask][idx_min]

    ax.plot(pd_min, Vb_min, 'o', color=C['accent'], ms=12, zorder=6,
            label=f'Minimum Paschen ≈ {int(Vb_min)} V')
    ax.axvline(pd_min, color=C['accent'], ls='--', lw=1.5, alpha=0.7)
    ax.axhline(Vb_min, color=C['accent'], ls='--', lw=1.5, alpha=0.7)

    ax.annotate(f'  Minimum de Paschen\n  p·d ≈ {pd_min:.1f} Pa·m\n  V ≈ {int(Vb_min)} V',
                xy=(pd_min, Vb_min), xytext=(pd_min*5, Vb_min+600),
                fontsize=10, color=C['hvred'],
                arrowprops=dict(arrowstyle='->', color=C['hvred'], lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    # Regions
    ax.axvspan(1, pd_min, alpha=0.04, color=C['hvred'])
    ax.axvspan(pd_min, 300, alpha=0.04, color=C['hvgreen'])
    ax.text(2, 2200, '← Vide / basse pression', fontsize=9.5,
            color=C['hvred'], style='italic')
    ax.text(40, 2200, 'Haute pression →', fontsize=9.5,
            color=C['hvgreen'], style='italic')

    ax.set_xlabel('Produit p·d  (Pa·m)', fontsize=12, labelpad=6)
    ax.set_ylabel('Tension de claquage $V_b$ (V)', fontsize=12, labelpad=6)
    ax.set_title('Courbe de Paschen — Tension de claquage dans l\'air\n'
                 '(coefficients Townsend : A=11.5 Pa⁻¹m⁻¹, B=364 V·Pa⁻¹m⁻¹, γ=0.01)',
                 fontsize=13, color=C['darkblue'], fontweight='bold', pad=12)
    ax.legend(fontsize=11, framealpha=0.9, loc='upper right')
    ax.set_ylim(0, 3000); ax.set_xlim(1, 300)
    ax.grid(True, alpha=0.3, ls='--', which='both')
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    save(fig, 'fig_paschen')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 3 — Corona effect
# ─────────────────────────────────────────────────────────────────────────────
def fig_corona():
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('#080818')
    ax.set_facecolor('#080818')
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4.5)
    ax.set_aspect('equal')

    # Glow layers (plasma)
    for r in np.linspace(0.35, 2.8, 30):
        alpha = 0.55 * np.exp(-((r - 0.6)/0.9)**2)
        b_int = int(min(255, 100 + 155*(2.8-r)/2.45))
        g_int = int(min(255, 50 + 80*(2.8-r)/2.45))
        col = f'#{0x1A:02x}{g_int:02x}{b_int:02x}'
        circle = plt.Circle((0,0), r, fill=False, color=col, lw=r*0.9+0.5, alpha=alpha)
        ax.add_patch(circle)

    # Field lines
    for angle in np.linspace(0, 360, 18, endpoint=False):
        rad = np.radians(angle)
        ax.annotate('', xy=(3.0*np.cos(rad), 3.0*np.sin(rad)),
                    xytext=(0.32*np.cos(rad), 0.32*np.sin(rad)),
                    arrowprops=dict(arrowstyle='->', color='#5090CC',
                                   lw=1.3, alpha=0.65, mutation_scale=12))

    # Ion/electron markers
    rng = np.random.default_rng(42)
    for _ in range(60):
        r = rng.uniform(0.4, 1.8)
        a = rng.uniform(0, 2*np.pi)
        ax.plot(r*np.cos(a), r*np.sin(a), '*', color='#FFD060',
                ms=rng.uniform(3, 7), alpha=0.85)

    # Conductor
    conductor = plt.Circle((0,0), 0.3, color='#D0D0D0', zorder=10)
    ax.add_patch(conductor)
    ax.text(0, 0, 'HT', fontsize=10, ha='center', va='center',
            color=C['darkblue'], fontweight='bold', zorder=11)

    # Labels
    ax.text(0, 4.2, 'Effet Corona — Vue en coupe', ha='center', va='center',
            color='white', fontsize=14, fontweight='bold')
    ax.text(0, 3.7, 'Décharge couronne autour d\'un conducteur sous HT',
            ha='center', va='center', color='#90B4D8', fontsize=10.5)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='*', color='w', markerfacecolor='#FFD060',
               markersize=10, label='Ions / électrons libres'),
        Line2D([0], [0], color='#5090CC', lw=2, label='Lignes de champ E'),
        plt.Circle((0,0), 0.1, color='#2050AA', label='Halo corona (plasma)'),
    ]
    legend = ax.legend(handles=legend_elements, loc='lower right',
                       framealpha=0.3, labelcolor='white', fontsize=9.5,
                       facecolor='#0D1A2D')
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)

    fig.tight_layout()
    save(fig, 'fig_corona')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 4 — Impulse waveforms (lightning + switching)
# ─────────────────────────────────────────────────────────────────────────────
def fig_impulse():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    fig.patch.set_facecolor(C['lightgray'])

    # --- Lightning impulse 1.2/50 µs ---
    ax1 = axes[0]
    ax1.set_facecolor('#F0F4FF')
    t = np.linspace(0, 200, 2000)
    T1, T2 = 1.2, 50.0
    v = (1 - np.exp(-t/T1)) * np.exp(-t/T2)
    v = v / v.max()

    ax1.plot(t, v, color=C['hvred'], lw=2.5, label='Onde 1.2/50 µs')
    ax1.fill_between(t, v, alpha=0.08, color=C['hvred'])

    # Reference lines
    for level, color, label in [
        (1.0, C['accent'], '$U_{\\rm peak}$ (100%)'),
        (0.9, C['lightblue'], '90%'),
        (0.5, C['hvgreen'], '50% → queue $T_2$'),
        (0.3, C['midblue'], '30%'),
    ]:
        ax1.axhline(level, color=color, ls='--', lw=1.3, alpha=0.75, label=label)

    # T1 annotation
    t_90 = t[np.argmin(np.abs(v - 0.9))]
    ax1.annotate('', xy=(t_90, 0.9), xytext=(0, 0.9),
                 arrowprops=dict(arrowstyle='<->', color=C['hvred'], lw=1.5))
    ax1.text(t_90/2, 0.94, f'$T_1 = 1.2\\,\\mu$s', ha='center',
             fontsize=10, color=C['hvred'], fontweight='bold')

    # T2 annotation
    t_50 = t[np.argmin(np.abs(v[100:]-0.5))+100]
    ax1.annotate('', xy=(t_50, 0.5), xytext=(0, 0.5),
                 arrowprops=dict(arrowstyle='<->', color=C['hvgreen'], lw=1.5))
    ax1.text(t_50/2, 0.54, f'$T_2 = 50\\,\\mu$s', ha='center',
             fontsize=10, color=C['hvgreen'], fontweight='bold')

    ax1.set_xlim(-5, 200); ax1.set_ylim(-0.05, 1.18)
    ax1.set_xlabel('Temps (µs)', fontsize=12)
    ax1.set_ylabel('Tension normalisée $u/U_{\\rm peak}$', fontsize=12)
    ax1.set_title('Onde de choc foudre — 1.2/50 µs\n(IEC 60060-1)',
                  fontsize=12, color=C['darkblue'], fontweight='bold')
    ax1.legend(fontsize=9.5, framealpha=0.9, loc='upper right')
    ax1.grid(alpha=0.2, ls='--')

    # --- Switching impulse 250/2500 µs ---
    ax2 = axes[1]
    ax2.set_facecolor('#F0F4FF')
    t2 = np.linspace(0, 9000, 2000)
    T1s, T2s = 250.0, 2500.0
    v2 = (1 - np.exp(-t2/T1s)) * np.exp(-t2/T2s)
    v2 = v2 / v2.max()

    ax2.plot(t2, v2, color=C['midblue'], lw=2.5, label='Onde 250/2500 µs')
    ax2.fill_between(t2, v2, alpha=0.07, color=C['midblue'])

    ax2.axhline(1.0, color=C['accent'], ls='--', lw=1.3, alpha=0.8, label='Crête')
    ax2.axhline(0.9, color=C['lightblue'], ls=':', lw=1.3, alpha=0.7, label='90%')
    ax2.axhline(0.5, color=C['hvgreen'], ls='--', lw=1.3, alpha=0.8, label='50% → $T_2$')

    t2_90 = t2[np.argmin(np.abs(v2 - 0.9))]
    ax2.annotate('', xy=(t2_90, 0.9), xytext=(0, 0.9),
                 arrowprops=dict(arrowstyle='<->', color=C['midblue'], lw=1.5))
    ax2.text(t2_90/2, 0.94, f'$T_1 = 250\\,\\mu$s', ha='center',
             fontsize=10, color=C['midblue'], fontweight='bold')

    t2_50 = t2[np.argmin(np.abs(v2[200:]-0.5))+200]
    ax2.annotate('', xy=(t2_50, 0.5), xytext=(0, 0.5),
                 arrowprops=dict(arrowstyle='<->', color=C['hvgreen'], lw=1.5))
    ax2.text(t2_50/2, 0.54, f'$T_2 = 2500\\,\\mu$s', ha='center',
             fontsize=10, color=C['hvgreen'], fontweight='bold')

    ax2.set_xlim(-100, 9000); ax2.set_ylim(-0.05, 1.18)
    ax2.set_xlabel('Temps (µs)', fontsize=12)
    ax2.set_ylabel('Tension normalisée', fontsize=12)
    ax2.set_title('Onde de manœuvre — 250/2500 µs\n(IEC 60060-1)',
                  fontsize=12, color=C['darkblue'], fontweight='bold')
    ax2.legend(fontsize=9.5, framealpha=0.9, loc='upper right')
    ax2.grid(alpha=0.2, ls='--')

    fig.suptitle('Formes d\'Ondes Normalisées des Surtensions',
                 fontsize=14, color=C['darkblue'], fontweight='bold', y=1.01)
    fig.tight_layout(pad=2.5)
    save(fig, 'fig_impulse')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 5 — Marx generator schematic
# ─────────────────────────────────────────────────────────────────────────────
def fig_marx():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    fig.patch.set_facecolor(C['lightgray'])
    ax.set_facecolor('#F0F4FF')
    ax.set_xlim(-0.5, 15); ax.set_ylim(-1.8, 7)
    ax.axis('off')

    ax.set_title('Générateur de Marx — Principe (4 étages)\n'
                 'Phase charge: condensateurs en PARALLÈLE  →  Phase décharge: condensateurs en SÉRIE',
                 fontsize=12.5, color=C['darkblue'], fontweight='bold', pad=12)

    n = 4
    stage_colors = [C['lightblue'], C['midblue'], C['darkblue'], '#05152A']

    for i in range(n):
        x0 = i * 3.5 + 0.3

        # Stage box
        ax.add_patch(patches.FancyBboxPatch(
            (x0, 0.5), 1.4, 5.0, boxstyle='round,pad=0.1',
            facecolor=stage_colors[i], alpha=0.12, edgecolor=stage_colors[i], lw=1.5))

        # Capacitor symbol
        ax.plot([x0+0.7, x0+0.7], [1.0, 2.3], color=stage_colors[i], lw=2.5)
        ax.plot([x0+0.25, x0+1.15], [2.3, 2.3], color=stage_colors[i], lw=3.5)
        ax.plot([x0+0.25, x0+1.15], [2.7, 2.7], color=stage_colors[i], lw=3.5)
        ax.plot([x0+0.7, x0+0.7], [2.7, 4.5], color=stage_colors[i], lw=2.5)

        ax.text(x0+0.7, 4.8, f'$C_{i+1}$', ha='center', fontsize=14,
                color=stage_colors[i], fontweight='bold')
        ax.text(x0+0.7, 0.6, f'$V_c = 100\\,\\mathrm{{kV}}$', ha='center',
                fontsize=9, color=C['textmed'])

        # Spark gap (between stages)
        if i < n - 1:
            gap_x = x0 + 2.1
            # Upper electrode
            ax.plot(gap_x, 3.8, 'o', ms=14, color=C['hvred'], zorder=5)
            ax.plot(gap_x, 3.0, 'o', ms=14, color=C['hvred'], zorder=5)
            ax.plot([gap_x, gap_x], [3.0, 3.8], color=C['hvred'], lw=2.5, zorder=4)
            ax.text(gap_x+0.25, 3.4, 'EG', fontsize=10, color=C['hvred'],
                    fontweight='bold', va='center')

            # Spark (zigzag)
            spark_x = [gap_x-0.15, gap_x-0.05, gap_x+0.05, gap_x+0.15, gap_x+0.05, gap_x-0.05]
            spark_y = [3.0, 3.25, 3.5, 3.55, 3.65, 3.8]
            ax.plot(spark_x, spark_y, color='#FFD040', lw=2.5, zorder=6, alpha=0.85)

            # Charging resistor (top)
            r_x = np.linspace(x0+0.7, x0+0.7+3.5, 12)
            r_y = np.array([4.5 + 0.25*np.sin(i*np.pi) for i in range(12)])
            ax.plot(r_x, r_y + 0.5, color=C['accent'], lw=2.5, zorder=3)
            ax.text((x0+0.7 + x0+4.2)/2, 5.35, '$R_c$', ha='center',
                    fontsize=10.5, color=C['accent'], fontweight='bold')

    # Waveshaping resistors
    out_x = n * 3.5 + 0.3
    ax.add_patch(patches.FancyBboxPatch(
        (out_x-0.1, 1.5), 1.0, 1.6, boxstyle='round,pad=0.1',
        facecolor=C['hvred'], alpha=0.15, edgecolor=C['hvred'], lw=1.5))
    ax.text(out_x+0.4, 2.3, '$R_1$\n(front)', ha='center', fontsize=10,
            color=C['hvred'], fontweight='bold')

    ax.add_patch(patches.FancyBboxPatch(
        (out_x-0.1, 3.5), 1.0, 1.4, boxstyle='round,pad=0.1',
        facecolor=C['hvgreen'], alpha=0.15, edgecolor=C['hvgreen'], lw=1.5))
    ax.text(out_x+0.4, 4.2, '$R_2$\n(queue)', ha='center', fontsize=10,
            color=C['hvgreen'], fontweight='bold')

    # Output arrow
    ax.annotate('', xy=(out_x+2.5, 3.0), xytext=(out_x+1.1, 3.0),
                arrowprops=dict(arrowstyle='->', color=C['hvred'],
                                lw=3.0, mutation_scale=22))
    ax.add_patch(patches.FancyBboxPatch(
        (out_x+2.5, 2.3), 2.5, 1.4, boxstyle='round,pad=0.15',
        facecolor='white', edgecolor=C['hvred'], lw=2))
    ax.text(out_x+3.75, 3.15, '$V_{\\rm out}$', ha='center', fontsize=12,
            color=C['hvred'], fontweight='bold')
    ax.text(out_x+3.75, 2.7, f'$= n \\times V_c = 400\\,\\mathrm{{kV}}$',
            ha='center', fontsize=10.5, color=C['hvred'])

    # Ground line
    ax.plot([0.3+0.7, 0.3+0.7], [0.5, 0.5-0.4], color=C['darkblue'], lw=2.5)
    ax.plot([0.5, 1.5], [0.1, 0.1], color=C['darkblue'], lw=3)
    ax.plot([0.7, 1.3], [-0.15, -0.15], color=C['darkblue'], lw=2)
    ax.plot([0.9, 1.1], [-0.4, -0.4], color=C['darkblue'], lw=1.5)

    # Phase labels
    ax.add_patch(patches.FancyBboxPatch(
        (0.2, -1.7), 13.5, 0.9, boxstyle='round,pad=0.1',
        facecolor=C['boxbg'], edgecolor=C['lightblue'], lw=1.2))
    ax.text(7.0, -1.3,
            'Charge: condensateurs en PARALLÈLE (chacun → $V_c$)   |   '
            'Décharge: éclateurs s\'amorçent en cascade → condensateurs en SÉRIE → $V_{\\rm out} = n\\,V_c$',
            ha='center', fontsize=9.5, color=C['darkblue'])

    fig.tight_layout()
    save(fig, 'fig_marx')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 6 — Insulation coordination bar chart
# ─────────────────────────────────────────────────────────────────────────────
def fig_insulation_coordination():
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor(C['lightgray'])
    ax.set_facecolor('#F0F4FF')

    labels = ['$U_n$\n(nominale)', '$U_m$\n(max. équip.)',
              '$U_s$\n(surtension)', '$U_p$\n(parafoudre)',
              'NIL manœuvre', 'NIL foudre']
    values = [400, 420, 700, 840, 1050, 1300]
    colors_bar = [C['hvgreen'], C['midblue'], C['accent'],
                  C['hvred'], C['lightblue'], C['darkblue']]

    bars = ax.bar(labels, values, color=colors_bar, width=0.6, alpha=0.88,
                  edgecolor='white', linewidth=1.5, zorder=3)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 18,
                f'{val} kV', ha='center', fontsize=11,
                color=C['textdark'], fontweight='bold')

    # Arrows showing margins
    for i in range(len(values)-1):
        ax.annotate('', xy=(i+1, values[i+1]*0.92),
                    xytext=(i, values[i]*1.05),
                    arrowprops=dict(arrowstyle='->', color='gray',
                                   lw=1.2, alpha=0.5))

    ax.set_ylabel('Tension (kV)', fontsize=12)
    ax.set_title('Coordination de l\'Isolation — Réseau 400 kV\n'
                 'Hiérarchie des tensions caractéristiques (IEC 60071)',
                 fontsize=13, color=C['darkblue'], fontweight='bold', pad=12)
    ax.set_ylim(0, 1550)
    ax.grid(axis='y', alpha=0.3, ls='--', zorder=0)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Annotations
    ax.text(5, 1430, 'NIL = Niveau d\'Isolation normalisé\n'
            '(Basic Insulation Level — BIL)',
            fontsize=9.5, color=C['darkblue'], style='italic',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor=C['lightblue']))

    fig.tight_layout()
    save(fig, 'fig_insulation_coord')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 7 — Coaxial cable field distribution
# ─────────────────────────────────────────────────────────────────────────────
def fig_coaxial_field():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor(C['lightgray'])

    a = 1.0   # inner radius
    R = 5.0   # outer radius
    U = 100   # kV

    r = np.linspace(a, R, 500)
    E = U / (r * np.log(R/a))

    # --- E(r) profile ---
    ax1 = axes[0]
    ax1.set_facecolor('#F0F4FF')
    ax1.plot(r, E, color=C['darkblue'], lw=2.8, label=r'$E(r) = U/[r\ln(R/a)]$')
    ax1.fill_between(r, E, alpha=0.08, color=C['hvred'])

    E_max = U / (a * np.log(R/a))
    ax1.plot(a, E_max, 'o', color=C['hvred'], ms=10, zorder=5,
             label=f'$E_{{\\rm max}} = {E_max:.1f}$ kV/m à $r=a$')
    ax1.axhline(E_max, color=C['hvred'], ls='--', lw=1.3, alpha=0.7)

    # Critical field line
    E_crit = 3.0  # MV/m → 3000 kV/m (scaled for this example: 30 kV/m)
    ax1.axhline(30, color=C['accent'], ls=':', lw=2, alpha=0.8,
                label='$E_{\\rm critique}$ (claquage air)')
    ax1.text(3.5, 31, 'Zone de claquage', fontsize=9, color=C['accent'])

    ax1.set_xlabel('Rayon $r$ (m)', fontsize=12)
    ax1.set_ylabel('Champ électrique $E(r)$ (kV/m)', fontsize=12)
    ax1.set_title('Champ dans un câble coaxial\n'
                  r'$a = 1\,\rm m$, $R = 5\,\rm m$, $U = 100\,\rm kV$',
                  fontsize=12, color=C['darkblue'], fontweight='bold')
    ax1.axvspan(a, a+0.3, alpha=0.15, color=C['hvred'])
    ax1.text(a+0.15, E_max*0.6, 'Risque\nmaxi', fontsize=8.5,
             ha='center', color=C['hvred'])
    ax1.legend(fontsize=9.5, framealpha=0.9)
    ax1.grid(alpha=0.25, ls='--')

    # --- Cross-section view ---
    ax2 = axes[1]
    ax2.set_facecolor('#0A1A2E')
    ax2.set_aspect('equal')
    ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 6.5)

    # Insulation
    insul = plt.Circle((0,0), R, color='#2A4A1A', alpha=0.6, zorder=1)
    ax2.add_patch(insul)
    # Inner conductor
    inner = plt.Circle((0,0), a, color='#A0A0C0', zorder=4)
    ax2.add_patch(inner)
    # Outer conductor
    outer_ring = plt.Circle((0,0), R, fill=False,
                              color='#808090', lw=4, zorder=5)
    ax2.add_patch(outer_ring)

    # Color map for E field intensity
    theta = np.linspace(0, 2*np.pi, 200)
    for r_val in np.linspace(a, R-0.1, 20):
        E_val = U / (r_val * np.log(R/a))
        # Map E to color: high E = red, low E = blue
        norm_E = (E_val - E[-1]) / (E[0] - E[-1])
        ring_color = plt.cm.RdYlBu_r(norm_E * 0.8 + 0.1)
        ring = plt.Circle((0,0), r_val, fill=False, color=ring_color,
                          lw=0.8, alpha=0.7, zorder=2)
        ax2.add_patch(ring)

    # Radial arrows
    for angle in np.linspace(0, 360, 12, endpoint=False):
        rad = np.radians(angle)
        ax2.annotate('', xy=(1.8*np.cos(rad), 1.8*np.sin(rad)),
                     xytext=(1.1*np.cos(rad), 1.1*np.sin(rad)),
                     arrowprops=dict(arrowstyle='->', color='#FF8080',
                                     lw=1.5, alpha=0.9, mutation_scale=10))
    for angle in np.linspace(0, 360, 12, endpoint=False):
        rad = np.radians(angle)
        ax2.annotate('', xy=(4.5*np.cos(rad), 4.5*np.sin(rad)),
                     xytext=(3.8*np.cos(rad), 3.8*np.sin(rad)),
                     arrowprops=dict(arrowstyle='->', color='#6080FF',
                                     lw=1.2, alpha=0.7, mutation_scale=8))

    ax2.text(0, 0, 'HT', ha='center', va='center', color='white',
             fontsize=11, fontweight='bold', zorder=6)
    ax2.text(0, 5.5, 'Vue en coupe — câble coaxial', ha='center',
             color='white', fontsize=11, fontweight='bold')
    ax2.text(0, -5.5, '← E fort (rouge) au centre | E faible (bleu) en périphérie →',
             ha='center', color='#90B4D8', fontsize=9)
    ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values(): sp.set_visible(False)

    fig.suptitle('Distribution du Champ Électrique dans un Câble Coaxial',
                 fontsize=14, color=C['darkblue'], fontweight='bold', y=1.01)
    fig.tight_layout(pad=2.0)
    save(fig, 'fig_coaxial_field')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 8 — Partial discharge model
# ─────────────────────────────────────────────────────────────────────────────
def fig_partial_discharge():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor(C['lightgray'])

    # --- Left: Physical model ---
    ax1 = axes[0]
    ax1.set_facecolor('#F0F4FF')
    ax1.set_xlim(-1, 9); ax1.set_ylim(-1.5, 5.5)
    ax1.axis('off')

    # Electrodes
    ax1.add_patch(patches.Rectangle((0, 4.0), 8, 0.7,
                                     color=C['darkblue'], zorder=3))
    ax1.add_patch(patches.Rectangle((0, -0.7), 8, 0.7,
                                     color=C['darkblue'], zorder=3))
    ax1.text(4, 4.85, 'Électrode HT (+)', ha='center', fontsize=11,
             color=C['darkblue'], fontweight='bold')
    ax1.text(4, -1.15, 'Électrode GND (−)', ha='center', fontsize=11,
             color=C['darkblue'], fontweight='bold')

    # Dielectric
    ax1.add_patch(patches.FancyBboxPatch(
        (0, 0), 8, 4, boxstyle='square',
        facecolor=C['accent'], alpha=0.12, edgecolor=C['midblue'], lw=1.5))
    ax1.text(1, 3.4, 'Diélectrique', fontsize=11, color=C['midblue'], fontweight='bold')
    ax1.text(1, 3.0, 'solide/liquide', fontsize=10, color=C['textmed'])

    # Cavity
    cavity = patches.Ellipse((4, 2.0), 2.5, 0.9,
                               facecolor='#C8E0FF', edgecolor=C['hvred'],
                               linewidth=2.5, zorder=4)
    ax1.add_patch(cavity)
    ax1.text(4, 2.0, 'Cavité gazeuse', ha='center', va='center',
             fontsize=9.5, color=C['hvred'], fontweight='bold', zorder=5)

    # Discharge in cavity
    disch_x = [3.2, 3.5, 3.3, 3.7, 3.9, 4.2, 4.1, 4.5, 4.7, 4.8]
    disch_y = [2.0, 2.25, 2.0, 2.2, 1.9, 2.15, 2.0, 2.2, 2.0, 2.0]
    ax1.plot(disch_x, disch_y, color='#FFD040', lw=3, zorder=6, alpha=0.9)
    ax1.text(4, 2.9, 'DP → érosion progressive', ha='center',
             fontsize=9.5, color=C['hvred'], style='italic')

    # Electric field arrows (in void)
    for x in [3.5, 4.0, 4.5]:
        ax1.annotate('', xy=(x, 0.3), xytext=(x, 3.7),
                     arrowprops=dict(arrowstyle='->', color=C['lightblue'],
                                     lw=1.2, alpha=0.5, mutation_scale=10))

    ax1.set_title('Modèle physique — Décharge partielle\ndans une cavité gazeuse',
                  fontsize=12, color=C['darkblue'], fontweight='bold', y=1.02)

    # --- Right: Equivalent circuit ---
    ax2 = axes[1]
    ax2.set_facecolor('#F0F4FF')
    ax2.set_xlim(-1, 7); ax2.set_ylim(-1, 6)
    ax2.axis('off')
    ax2.set_title('Circuit équivalent — Modèle à 3 capacités\n(Gemant-Philipps)',
                  fontsize=12, color=C['darkblue'], fontweight='bold', y=1.02)

    # Draw circuit
    # V source
    ax2.add_patch(plt.Circle((1.0, 3.0), 0.55, fill=False,
                               color=C['accent'], lw=2.5, zorder=4))
    ax2.text(1.0, 3.0, '~\n$V$', ha='center', va='center',
             fontsize=10, color=C['accent'])
    ax2.plot([1.0, 1.0], [3.55, 5.0], color=C['darkblue'], lw=2.5)
    ax2.plot([1.0, 1.0], [2.45, 1.0], color=C['darkblue'], lw=2.5)
    ax2.plot([1.0, 3.0], [5.0, 5.0], color=C['darkblue'], lw=2.5)
    ax2.plot([1.0, 3.0], [1.0, 1.0], color=C['darkblue'], lw=2.5)

    def draw_cap(ax, x, y, label):
        ax.plot([x, x], [y, y+0.5], color=C['midblue'], lw=2.5)
        ax.plot([x-0.4, x+0.4], [y+0.5, y+0.5], color=C['midblue'], lw=3.5)
        ax.plot([x-0.4, x+0.4], [y+0.7, y+0.7], color=C['midblue'], lw=3.5)
        ax.plot([x, x], [y+0.7, y+1.2], color=C['midblue'], lw=2.5)
        ax.text(x+0.6, y+0.6, label, fontsize=11, color=C['midblue'], fontweight='bold')

    # Ca (series)
    draw_cap(ax2, 3.0, 3.4, '$C_a$')
    ax2.plot([3.0, 3.0], [5.0, 4.6], color=C['darkblue'], lw=2.5)
    ax2.plot([3.0, 3.0], [3.4, 3.0], color=C['darkblue'], lw=2.5)
    ax2.text(3.7, 2.7, '(série)', fontsize=9, color=C['textmed'])

    # Cb (cavity) + spark gap
    draw_cap(ax2, 3.0, 1.5, '$C_b$')
    ax2.add_patch(plt.Circle((3.0, 2.9), 0.2, color=C['hvred'], alpha=0.8, zorder=5))
    ax2.text(3.7, 2.1, '(cavité)', fontsize=9, color=C['textmed'])

    ax2.plot([3.0, 3.0], [3.0, 2.7], color=C['darkblue'], lw=2.5)
    ax2.plot([3.0, 3.0], [1.5, 1.0], color=C['darkblue'], lw=2.5)

    # Cc (parallel)
    draw_cap(ax2, 5.0, 2.9, '$C_c$')
    ax2.plot([3.0, 5.0], [5.0, 5.0], color=C['darkblue'], lw=2.5)
    ax2.plot([5.0, 5.0], [5.0, 4.1], color=C['darkblue'], lw=2.5)
    ax2.plot([5.0, 5.0], [2.9, 1.0], color=C['darkblue'], lw=2.5)
    ax2.plot([3.0, 5.0], [1.0, 1.0], color=C['darkblue'], lw=2.5)
    ax2.text(5.7, 3.5, '(parallèle)', fontsize=9, color=C['textmed'])

    ax2.text(3.0, 0.3, '$Q_{\\rm DP} = C_b \\times \\Delta V_{\\rm cav}$  [pC]',
             ha='center', fontsize=11, color=C['darkblue'], fontweight='bold',
             bbox=dict(facecolor=C['boxbg'], edgecolor=C['lightblue'],
                       boxstyle='round,pad=0.3'))

    fig.suptitle('Décharges Partielles — Modèle et Circuit Équivalent',
                 fontsize=14, color=C['darkblue'], fontweight='bold', y=1.01)
    fig.tight_layout(pad=2.0)
    save(fig, 'fig_partial_discharge')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 9 — Sphere gap diagram
# ─────────────────────────────────────────────────────────────────────────────
def fig_sphere_gap():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(C['lightgray'])
    ax.set_facecolor('#F0F4FF')
    ax.set_xlim(-2, 12); ax.set_ylim(-2.5, 4)
    ax.axis('off')

    ax.set_title('Éclateur à Sphères — IEC 60052\nMesure de la valeur crête de haute tension',
                 fontsize=13, color=C['darkblue'], fontweight='bold', pad=10)

    # HV sphere
    hv_sphere = plt.Circle((2.0, 0.5), 1.5, color=C['midblue'], alpha=0.7, zorder=3)
    ax.add_patch(hv_sphere)
    hv_highlight = plt.Circle((1.5, 1.0), 0.35, color='white', alpha=0.3, zorder=4)
    ax.add_patch(hv_highlight)
    ax.text(2.0, 0.5, 'HT', ha='center', va='center',
            color='white', fontsize=13, fontweight='bold', zorder=5)

    # GND sphere
    gnd_sphere = plt.Circle((8.0, 0.5), 1.5, color=C['darkblue'], alpha=0.8, zorder=3)
    ax.add_patch(gnd_sphere)
    gnd_highlight = plt.Circle((7.5, 1.0), 0.35, color='white', alpha=0.25, zorder=4)
    ax.add_patch(gnd_highlight)
    ax.text(8.0, 0.5, 'GND', ha='center', va='center',
            color='white', fontsize=12, fontweight='bold', zorder=5)

    # Gap dimension arrow
    ax.annotate('', xy=(6.5, 0.5), xytext=(3.5, 0.5),
                arrowprops=dict(arrowstyle='<->', color=C['accent'], lw=2.5,
                                mutation_scale=16))
    ax.text(5.0, 1.0, '$d$', ha='center', fontsize=16,
            color=C['accent'], fontweight='bold', style='italic')

    # Sphere diameter
    ax.annotate('', xy=(3.5, -1.5), xytext=(0.5, -1.5),
                arrowprops=dict(arrowstyle='<->', color=C['midblue'], lw=2.0,
                                mutation_scale=12))
    ax.text(2.0, -1.85, '$D$ (diamètre)', ha='center', fontsize=11,
            color=C['midblue'], style='italic')

    # Spark
    spark_x = np.array([3.6, 3.9, 3.7, 4.1, 3.9, 4.3, 4.1, 4.5, 4.3, 4.7, 4.5, 4.8, 5.0,
                         5.2, 5.0, 5.4, 5.2, 5.6, 5.4, 5.7, 5.9, 6.1, 6.3, 6.4])
    spark_y = np.array([0.5, 0.8, 0.3, 0.7, 0.4, 0.8, 0.3, 0.75, 0.45, 0.8, 0.5, 0.75,
                         0.5, 0.85, 0.45, 0.8, 0.4, 0.78, 0.5, 0.8, 0.5, 0.78, 0.55, 0.5])
    ax.plot(spark_x, spark_y, color='#FFD040', lw=3.5, zorder=6, alpha=0.95)

    # HV connection
    ax.plot([2.0, 2.0], [2.0, 3.5], color=C['hvred'], lw=2.5)
    ax.text(2.0, 3.7, '$V_{\\rm HT}$ (à mesurer)', ha='center',
            fontsize=11, color=C['hvred'], fontweight='bold')

    # GND connection
    ax.plot([8.0, 8.0], [2.0, 2.5], color=C['darkblue'], lw=2.5)
    ax.plot([7.3, 8.7], [2.5, 2.5], color=C['darkblue'], lw=3)
    ax.plot([7.5, 8.5], [2.8, 2.8], color=C['darkblue'], lw=2)
    ax.plot([7.7, 8.3], [3.1, 3.1], color=C['darkblue'], lw=1.5)

    # Formula box
    ax.add_patch(patches.FancyBboxPatch(
        (9.2, -1.0), 2.4, 2.8, boxstyle='round,pad=0.15',
        facecolor=C['boxbg'], edgecolor=C['lightblue'], lw=1.8))
    ax.text(10.4, 1.5, 'IEC 60052', ha='center', fontsize=10,
            color=C['darkblue'], fontweight='bold')
    ax.text(10.4, 1.0, '$V_b = V_{\\rm table}(D,d)$', ha='center',
            fontsize=10.5, color=C['darkblue'])
    ax.text(10.4, 0.45, 'Corrigé : $\\delta = \\frac{p \\times 293}{101.3 \\times T}$',
            ha='center', fontsize=9.5, color=C['darkblue'])
    ax.text(10.4, -0.15, '$V = V_{\\rm table} \\times \\delta$', ha='center',
            fontsize=10, color=C['hvred'], fontweight='bold')
    ax.text(10.4, -0.65, 'Précision : $\\pm 3\\%$', ha='center',
            fontsize=9.5, color=C['textmed'])

    fig.tight_layout()
    save(fig, 'fig_sphere_gap')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 10 — Townsend ionization process
# ─────────────────────────────────────────────────────────────────────────────
def fig_townsend():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(C['lightgray'])
    ax.set_facecolor('#0A0A1E')
    ax.set_xlim(-0.5, 8.5); ax.set_ylim(-1.5, 5.5)
    ax.axis('off')
    ax.set_title('Mécanisme d\'Avalanche de Townsend', fontsize=14,
                 color=C['darkblue'], fontweight='bold', y=1.02)

    # Electrodes
    ax.add_patch(patches.Rectangle((-0.5, 0), 0.5, 4.5, color='#505070', zorder=3))
    ax.add_patch(patches.Rectangle((8.0, 0), 0.5, 4.5, color='#703020', zorder=3))
    ax.text(-0.5, 4.8, 'Cathode (−)', fontsize=10, color='#A0A0C0', fontweight='bold')
    ax.text(7.5, 4.8, 'Anode (+)', fontsize=10, color='#C08060', fontweight='bold')

    # E field arrows (background)
    for y in np.linspace(0.5, 4.0, 5):
        ax.annotate('', xy=(7.8, y), xytext=(0.1, y),
                    arrowprops=dict(arrowstyle='->', color='#3050A0',
                                   lw=1.0, alpha=0.35, mutation_scale=8))

    # Initial electron (from cathode)
    ax.plot(0.2, 2.5, 'o', ms=12, color='#60A0FF', zorder=5)
    ax.text(0.3, 2.9, '$e_0$\n(initial)', fontsize=9, color='#60A0FF')

    # Avalanche tree
    positions = {0: [(1.0, 2.5)]}
    for gen in range(1, 4):
        positions[gen] = []
        for x0, y0 in positions[gen-1]:
            dx = 1.8
            dy_spread = 0.7 * (0.6 ** gen)
            for dy in [-dy_spread, +dy_spread]:
                nx, ny = x0+dx, y0+dy
                if 0.2 < ny < 4.3:
                    positions[gen].append((nx, ny))
                    # Draw arrow
                    ax.annotate('', xy=(nx, ny), xytext=(x0, y0),
                                arrowprops=dict(arrowstyle='->', color='#6080FF',
                                               lw=1.5, mutation_scale=12, alpha=0.8))
                    # Ion marker
                    mid_x = (x0+nx)/2
                    mid_y = (y0+ny)/2 + 0.2
                    ax.plot(mid_x, mid_y, '+', ms=10, color='#FF6060',
                            markeredgewidth=2.5, zorder=5, alpha=0.8)

    # Final electrons
    for gen in range(4):
        for x, y in positions[gen]:
            ax.plot(x, y, 'o', ms=8, color='#60A0FF', zorder=5, alpha=0.9)

    # Generation labels
    gen_x = [1.0, 2.8, 4.6, 6.4]
    for i, x in enumerate(gen_x):
        ax.text(x, -0.6, f'Gen. {i}', ha='center', fontsize=9.5,
                color='#90A0CC', fontweight='bold')
        ax.axvline(x, color='white', lw=0.5, alpha=0.1, ls='--')

    # Legend
    ax.plot([], [], 'o', ms=8, color='#60A0FF', label='Électron')
    ax.plot([], [], '+', ms=10, color='#FF6060', markeredgewidth=2.5, label='Ion +')
    ax.plot([], [], '->', color='#6060AA', label='Trajectoire ionisante')
    legend = ax.legend(loc='lower right', fontsize=9.5, framealpha=0.4,
                       labelcolor='white', facecolor='#1A1A3A')

    ax.text(4, -1.2, r'Condition de claquage : $\gamma\,(e^{\alpha d}-1) = 1$',
            ha='center', fontsize=11, color='#FFD060',
            bbox=dict(facecolor='#1A1A3A', alpha=0.8, edgecolor='#FFD060'))

    fig.tight_layout()
    save(fig, 'fig_townsend')


# ─────────────────────────────────────────────────────────────────────────────
# FIG 11 — Voltage divider schematic
# ─────────────────────────────────────────────────────────────────────────────
def fig_voltage_divider():
    fig, axes = plt.subplots(1, 3, figsize=(13, 6))
    fig.patch.set_facecolor(C['lightgray'])

    titles = ['Diviseur Résistif\n(DC / AC basse fréq.)',
              'Diviseur Capacitif\n(AC / Impulsions)',
              'Diviseur Résistif-Capacitif\n(RC — Impulsions)']
    r_colors = [C['hvred'], C['midblue'], C['hvgreen']]
    types = ['R', 'C', 'RC']

    for idx, (ax, title, col, typ) in enumerate(zip(axes, titles, r_colors, types)):
        ax.set_facecolor('#F0F4FF')
        ax.set_xlim(-1.5, 5); ax.set_ylim(-2, 9)
        ax.axis('off')
        ax.set_title(title, fontsize=11.5, color=C['darkblue'], fontweight='bold', pad=8)

        # HV input
        ax.annotate('', xy=(1.5, 7.8), xytext=(1.5, 9.0),
                    arrowprops=dict(arrowstyle='->', color=C['hvred'], lw=2.5,
                                   mutation_scale=14))
        ax.text(1.5, 9.1, '$V_{\\rm HT}$', ha='center', fontsize=12,
                color=C['hvred'], fontweight='bold')

        # Z1 (HV side)
        ax.add_patch(patches.FancyBboxPatch(
            (0.8, 5.5), 1.4, 2.2, boxstyle='round,pad=0.15',
            facecolor=col, alpha=0.18, edgecolor=col, lw=2.0))
        ax.text(1.5, 6.6, f'$Z_1$\n({typ})', ha='center', fontsize=12,
                color=col, fontweight='bold')
        ax.text(1.5, 5.2, '(HV)', ha='center', fontsize=9, color=C['textmed'])
        ax.plot([1.5, 1.5], [7.8, 7.7], color=C['darkblue'], lw=2.5)
        ax.plot([1.5, 1.5], [5.5, 5.2], color=C['darkblue'], lw=2.5)

        # Z2 (LV side)
        ax.add_patch(patches.FancyBboxPatch(
            (0.8, 2.5), 1.4, 2.2, boxstyle='round,pad=0.15',
            facecolor=C['hvgreen'], alpha=0.18, edgecolor=C['hvgreen'], lw=2.0))
        ax.text(1.5, 3.6, f'$Z_2$\n({typ})', ha='center', fontsize=12,
                color=C['hvgreen'], fontweight='bold')
        ax.text(1.5, 2.2, '(LV)', ha='center', fontsize=9, color=C['textmed'])
        ax.plot([1.5, 1.5], [5.2, 4.7], color=C['darkblue'], lw=2.5)
        ax.plot([1.5, 1.5], [2.5, 2.2], color=C['darkblue'], lw=2.5)

        # GND
        ax.plot([0.9, 2.1], [2.0, 2.0], color=C['darkblue'], lw=3)
        ax.plot([1.1, 1.9], [1.7, 1.7], color=C['darkblue'], lw=2)
        ax.plot([1.3, 1.7], [1.4, 1.4], color=C['darkblue'], lw=1.5)

        # Measurement point
        ax.plot(1.5, 4.95, 'o', ms=10, color=C['accent'], zorder=5)
        ax.plot([1.5, 3.5], [4.95, 4.95], color=C['accent'], lw=2, ls='--')
        ax.plot([3.5, 3.5], [2.0, 4.95], color=C['accent'], lw=2, ls='--')
        ax.plot(3.5, 2.0, 'o', ms=7, color=C['accent'], zorder=5)

        # Voltmeter
        vm = plt.Circle((3.8, 3.4), 0.6, fill=False,
                          color=C['accent'], lw=2.5, zorder=4)
        ax.add_patch(vm)
        ax.text(3.8, 3.4, 'V', ha='center', va='center',
                fontsize=13, color=C['accent'], fontweight='bold')
        ax.text(3.8, 2.55, '$V_m$', ha='center', fontsize=10,
                color=C['accent'])

        # Formula
        ax.add_patch(patches.FancyBboxPatch(
            (-1.3, -1.8), 4.5, 1.3, boxstyle='round,pad=0.1',
            facecolor=C['boxbg'], edgecolor=C['lightblue'], lw=1.2))
        ax.text(0.95, -0.95, f'$k = (Z_1+Z_2)/Z_2$', ha='center',
                fontsize=10.5, color=C['darkblue'], fontweight='bold')
        ax.text(0.95, -1.45, f'$V_{{\\rm HT}} = k \\times V_m$', ha='center',
                fontsize=10.5, color=C['darkblue'])

    fig.suptitle('Diviseurs de Tension Haute Tension — Types et Schémas',
                 fontsize=14, color=C['darkblue'], fontweight='bold', y=1.01)
    fig.tight_layout(pad=2.0)
    save(fig, 'fig_voltage_divider')


# ─────────────────────────────────────────────────────────────────────────────
# RUN ALL
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Generating HV Engineering figures...")
    fig_electric_field()
    fig_paschen()
    fig_corona()
    fig_impulse()
    fig_marx()
    fig_insulation_coordination()
    fig_coaxial_field()
    fig_partial_discharge()
    fig_sphere_gap()
    fig_townsend()
    fig_voltage_divider()
    print(f"\nDone! All figures saved in '{FIGDIR}/'")
    print("\nTo compile the LaTeX document:")
    print("  1. Run:  python generate_figures.py")
    print("  2. Then: pdflatex main.tex")
    print("  3. Then: pdflatex main.tex  (twice for TOC)")
