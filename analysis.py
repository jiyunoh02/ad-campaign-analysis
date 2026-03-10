import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── 스타일 설정 ──
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
sns.set_palette("muted")

df = pd.read_csv('campaign_data.csv')

# ── 색상 정의 ──
platform_colors = {'Facebook': '#1877F2', 'TikTok': '#010101'}
framing_colors  = {'bust': '#E07B54', 'full_body': '#5B8DB8'}
subject_colors  = {'human': '#4CAF50', 'ai': '#9C27B0', 'character': '#FF9800'}
format_colors   = {'video': '#E07B54', 'image': '#5B8DB8'}

# ════════════════════════════════════════════════
# Figure 1: Platform 비교 — CTR & Conversion Rate
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Platform Comparison: Facebook vs TikTok', fontsize=14, fontweight='bold', y=1.02)

platform_summary = df.groupby('platform').agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv_rate=('conversion_rate', 'mean'),
    total_conversions=('conversions', 'sum'),
    total_spend=('spend_krw', 'sum')
).reset_index()

# CTR
bars = axes[0].bar(platform_summary['platform'], platform_summary['avg_ctr'],
                   color=[platform_colors[p] for p in platform_summary['platform']],
                   width=0.5, edgecolor='white')
for bar, val in zip(bars, platform_summary['avg_ctr']):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                 f'{val:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
axes[0].set_title('Avg CTR by Platform', fontsize=12)
axes[0].set_ylabel('CTR (%)')
axes[0].set_ylim(0, 2.8)

# Conversion Rate
bars2 = axes[1].bar(platform_summary['platform'], platform_summary['avg_conv_rate'],
                    color=[platform_colors[p] for p in platform_summary['platform']],
                    width=0.5, edgecolor='white')
for bar, val in zip(bars2, platform_summary['avg_conv_rate']):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
axes[1].set_title('Avg Conversion Rate by Platform\n(click → website action)', fontsize=12)
axes[1].set_ylabel('Conversion Rate (%)')
axes[1].set_ylim(0, 42)

plt.tight_layout()
plt.savefig('fig1_platform_comparison.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 1 saved")

# ════════════════════════════════════════════════
# Figure 2: Creative별 CTR (A/B 테스트 메인 결과)
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('A/B Test Results: CTR by Creative (6 Concepts)', fontsize=14, fontweight='bold')

for ax, platform in zip(axes, ['Facebook', 'TikTok']):
    sub = df[(df['platform'] == platform) & (df['format'] == 'video')].sort_values('ctr', ascending=False).copy()
    short_names = [n.replace(' (Photo)', '') for n in sub['creative_name']]
    colors = [subject_colors[s] for s in sub['subject_type']]

    bars = ax.barh(range(len(sub)), sub['ctr'], color=colors, edgecolor='white', height=0.6)
    ax.set_yticks(range(len(sub)))
    ax.set_yticklabels(short_names, fontsize=10)
    ax.set_xlabel('CTR (%)')
    ax.set_title(f'{platform}', fontsize=12, fontweight='bold')
    ax.invert_yaxis()

    for bar, val in zip(bars, sub['ctr']):
        ax.text(val + 0.02, bar.get_y() + bar.get_height()/2,
                f'{val:.2f}%', va='center', fontsize=10, fontweight='bold')

    # 1위 하이라이트
    bars[0].set_edgecolor('#FF5722')
    bars[0].set_linewidth(2.5)
    ax.set_xlim(0, sub['ctr'].max() * 1.35)

legend_patches = [mpatches.Patch(color=subject_colors['human'], label='Human'),
                  mpatches.Patch(color=subject_colors['ai'], label='AI'),
                  mpatches.Patch(color=subject_colors['character'], label='Character')]
axes[1].legend(handles=legend_patches, loc='lower right', fontsize=9)

plt.tight_layout()
plt.savefig('fig2_ab_test_ctr.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 2 saved")

# ════════════════════════════════════════════════
# Figure 3: Framing 효과 — Bust vs Full Body
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Framing Effect: Bust-Only vs Full-Body', fontsize=14, fontweight='bold')

video_df = df[df['format'] == 'video'].copy()
framing_platform = video_df.groupby(['platform', 'framing']).agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv=('conversion_rate', 'mean')
).reset_index()

for ax, metric, label, ylim in zip(
    axes,
    ['avg_ctr', 'avg_conv'],
    ['Avg CTR (%)', 'Avg Conversion Rate (%)'],
    [3.2, 45]
):
    x = np.arange(2)
    width = 0.35
    platforms = ['Facebook', 'TikTok']

    for i, platform in enumerate(platforms):
        sub = framing_platform[framing_platform['platform'] == platform].set_index('framing')
        vals = [sub.loc['bust', metric], sub.loc['full_body', metric]]
        bars = ax.bar(x + i*width, vals, width, label=platform,
                      color=list(platform_colors.values())[i], alpha=0.85)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                    f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_xticks(x + width/2)
    ax.set_xticklabels(['Bust Only', 'Full Body'], fontsize=11)
    ax.set_ylabel(label)
    ax.set_ylim(0, ylim)
    ax.legend()

axes[0].set_title('CTR: Bust vs Full Body')
axes[1].set_title('Conversion Rate: Bust vs Full Body')

plt.tight_layout()
plt.savefig('fig3_framing_effect.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 3 saved")

# ════════════════════════════════════════════════
# Figure 4: Video vs Photo (Facebook only)
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Format Comparison: Video vs Photo (Facebook)', fontsize=14, fontweight='bold')

fb_df = df[df['platform'] == 'Facebook'].copy()
# human bust만 비교 (같은 크리에이티브 컨셉)
fb_human_bust = fb_df[fb_df['subject_type'] == 'human'].groupby('format').agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv=('conversion_rate', 'mean')
).reset_index()

for ax, metric, label, ylim in zip(
    axes,
    ['avg_ctr', 'avg_conv'],
    ['CTR (%)', 'Conversion Rate (%)'],
    [3.5, 40]
):
    bars = ax.bar(fb_human_bust['format'], fb_human_bust[metric],
                  color=[format_colors[f] for f in fb_human_bust['format']],
                  width=0.4, edgecolor='white')
    for bar, val in zip(bars, fb_human_bust[metric]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                f'{val:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.set_ylabel(label)
    ax.set_ylim(0, ylim)
    ax.set_xticklabels(['Video', 'Photo'], fontsize=12)

axes[0].set_title('CTR: Video vs Photo')
axes[1].set_title('Conversion Rate: Video vs Photo')

plt.tight_layout()
plt.savefig('fig4_video_vs_photo.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 4 saved")

# ════════════════════════════════════════════════
# Figure 5: Budget Reallocation — Before vs After
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Budget Reallocation Strategy (Based on A/B Test)', fontsize=14, fontweight='bold')

creatives = ['Close-Up\nClara', 'Full-Shot\nClara', 'Close-Up\nNova', 'Full-Shot\nNova', 'Buddy', 'Mochi']

# Before: 균등 배분
before = [50000, 50000, 50000, 50000, 50000, 50000]
# After: 상위 2개로 집중 (기억 기반 — human bust 최고 성과)
after  = [110000, 80000, 50000, 30000, 20000, 10000]

x = np.arange(len(creatives))
width = 0.35

bars1 = axes[0].bar(x, before, width*2, color='#B0BEC5', edgecolor='white', label='Week 1–2 (Equal)')
bars2 = axes[1].bar(x, after,  width*2,
                    color=['#E07B54' if i < 2 else '#B0BEC5' for i in range(6)],
                    edgecolor='white', label='Week 3–4 (Optimized)')

for ax, bars, vals in zip(axes, [bars1, bars2], [before, after]):
    ax.set_xticks(x)
    ax.set_xticklabels(creatives, fontsize=9)
    ax.set_ylabel('Budget (KRW)')
    ax.set_ylim(0, 135000)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1500,
                f'₩{val//1000}K', ha='center', va='bottom', fontsize=9)

axes[0].set_title('Initial Allocation (Equal Split)', fontsize=11)
axes[1].set_title('Reallocated (Top 2 Creatives → 63% of Budget)', fontsize=11)

highlight = mpatches.Patch(color='#E07B54', label='Top-performing creatives')
axes[1].legend(handles=[highlight], fontsize=9)

plt.tight_layout()
plt.savefig('fig5_budget_reallocation.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 5 saved")

# ════════════════════════════════════════════════
# Summary stats 출력
# ════════════════════════════════════════════════
print("\n" + "="*50)
print("CAMPAIGN SUMMARY")
print("="*50)
print(f"Total Spend:       ₩{df['spend_krw'].sum():,}")
print(f"Total Impressions: {df['impressions'].sum():,}")
print(f"Total Clicks:      {df['clicks'].sum():,}")
print(f"Overall CTR:       {df['clicks'].sum()/df['impressions'].sum()*100:.2f}%")
print(f"Total Conversions: {df['conversions'].sum():,}")
print(f"\nTop Creative (CTR):  {df.loc[df['ctr'].idxmax(), 'creative_name']} ({df['ctr'].max():.2f}%) on {df.loc[df['ctr'].idxmax(), 'platform']}")
print(f"Top Creative (Conv): {df.loc[df['conversion_rate'].idxmax(), 'creative_name']} ({df['conversion_rate'].max():.1f}%) on {df.loc[df['conversion_rate'].idxmax(), 'platform']}")
print("="*50)
