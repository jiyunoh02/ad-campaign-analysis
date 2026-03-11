import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

df = pd.read_csv('campaign_data.csv')
main_df    = df[df['experiment'] == 'main'].copy()
framing_df = df[df['experiment'] == 'framing'].copy()

platform_colors = {'Facebook': '#1877F2', 'TikTok': '#010101'}
model_colors    = {'influencer': '#E07B54', 'general': '#5B8DB8'}
framing_colors  = {'closeup': '#E07B54', 'fullshot': '#5B8DB8'}
model_labels    = {'influencer': 'Influencer', 'general': 'General'}
framing_labels  = {'closeup': 'Close-Up', 'fullshot': 'Full-Shot'}

# ════════════════════════════════════════════════
# Figure 1: 메인 실험 — CTR & Conversion Rate
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Main Experiment: Influencer vs General Close-Up', fontsize=14, fontweight='bold')

main_summary = main_df.groupby(['platform', 'model_type']).agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv=('conversion_rate', 'mean')
).reset_index()

import numpy as np
for ax, metric, label, ylim in zip(
    axes,
    ['avg_ctr', 'avg_conv'],
    ['Avg CTR (%)', 'Avg Conversion Rate (%)'],
    [4.0, 50]
):
    x = np.arange(2)
    width = 0.35
    for i, platform in enumerate(['Facebook', 'TikTok']):
        sub = main_summary[main_summary['platform'] == platform].set_index('model_type')
        vals = [sub.loc['influencer', metric], sub.loc['general', metric]]
        bars = ax.bar(x + i * width, vals, width,
                      label=platform,
                      color=list(platform_colors.values())[i],
                      alpha=0.85, edgecolor='white')
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(['Influencer', 'General'], fontsize=11)
    ax.set_ylabel(label)
    ax.set_ylim(0, ylim)
    ax.legend()

axes[0].set_title('CTR by Model Type & Platform')
axes[1].set_title('Conversion Rate by Model Type & Platform')

plt.tight_layout()
plt.savefig('figures/fig1_main_experiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 1 saved")

# ════════════════════════════════════════════════
# Figure 2: 주차별 CTR 추이 (시계열)
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Weekly CTR Trend: Before & After Budget Reallocation', fontsize=14, fontweight='bold')

weekly = main_df.groupby(['platform', 'model_type', 'week']).agg(
    avg_ctr=('ctr', 'mean')
).reset_index()
weekly['week'] = weekly['week'].astype(int)

for ax, platform in zip(axes, ['Facebook', 'TikTok']):
    sub = weekly[weekly['platform'] == platform]
    for model, color in model_colors.items():
        data = sub[sub['model_type'] == model].sort_values('week')
        ax.plot(data['week'], data['avg_ctr'],
                marker='o', color=color, linewidth=2.5, markersize=7,
                label=model_labels[model])

    # 예산 재배분 시점 표시
    ax.axvline(x=2.5, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(2.6, ax.get_ylim()[1] * 0.92 if ax.get_ylim()[1] > 0 else 3.5,
            'Budget\nReallocated', fontsize=8, color='gray')

    ax.set_title(platform, fontsize=12, fontweight='bold')
    ax.set_xlabel('Week')
    ax.set_ylabel('CTR (%)')
    ax.set_xlim(0.7, 4.5)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(['Week 1', 'Week 2', 'Week 3', 'Week 4'])
    ax.legend()

plt.tight_layout()
plt.savefig('figures/fig2_weekly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 2 saved")

# ════════════════════════════════════════════════
# Figure 3: 추가 실험 — 클로즈업 vs 전신 (Framing)
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Additional Experiment: Close-Up vs Full-Shot (Framing Effect)', fontsize=14, fontweight='bold')

framing_summary = framing_df.groupby(['platform', 'framing']).agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv=('conversion_rate', 'mean')
).reset_index()

for ax, metric, label, ylim in zip(
    axes,
    ['avg_ctr', 'avg_conv'],
    ['Avg CTR (%)', 'Avg Conversion Rate (%)'],
    [3.5, 45]
):
    x = np.arange(2)
    width = 0.35
    for i, platform in enumerate(['Facebook', 'TikTok']):
        sub = framing_summary[framing_summary['platform'] == platform].set_index('framing')
        vals = [sub.loc['closeup', metric], sub.loc['fullshot', metric]]
        bars = ax.bar(x + i * width, vals, width,
                      label=platform,
                      color=list(platform_colors.values())[i],
                      alpha=0.85, edgecolor='white')
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(['Close-Up', 'Full-Shot'], fontsize=11)
    ax.set_ylabel(label)
    ax.set_ylim(0, ylim)
    ax.legend()

axes[0].set_title('CTR by Framing & Platform')
axes[1].set_title('Conversion Rate by Framing & Platform')

plt.tight_layout()
plt.savefig('figures/fig3_framing_experiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 3 saved")

# ════════════════════════════════════════════════
# Figure 4: 종합 요약 Heatmap (2x2)
# ════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle('Summary Heatmap: CTR & Conversion Rate\n(Model Type × Platform)', fontsize=13, fontweight='bold')

main_agg = main_df.groupby(['platform', 'model_type']).agg(
    avg_ctr=('ctr', 'mean'),
    avg_conv=('conversion_rate', 'mean')
).reset_index()

for ax, metric, label in zip(
    axes,
    ['avg_ctr', 'avg_conv'],
    ['CTR (%)', 'Conversion Rate (%)']
):
    pivot = main_agg.pivot(index='model_type', columns='platform', values=metric)
    pivot.index = [model_labels[i] for i in pivot.index]
    sns.heatmap(pivot, annot=True, fmt='.2f', cmap='YlOrRd',
                ax=ax, linewidths=0.5, cbar_kws={'label': label})
    ax.set_title(label)
    ax.set_xlabel('')
    ax.set_ylabel('')

plt.tight_layout()
plt.savefig('figures/fig4_summary_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Fig 4 saved")

# ════════════════════════════════════════════════
# Summary
# ════════════════════════════════════════════════
print("\n" + "=" * 55)
print("CAMPAIGN SUMMARY")
print("=" * 55)
print(f"Total Spend:         ₩{df['spend_krw'].sum():,}")
print(f"Total Impressions:   {df['impressions'].sum():,}")
print(f"Total Clicks:        {df['clicks'].sum():,}")
print(f"Overall CTR:         {df['clicks'].sum()/df['impressions'].sum()*100:.2f}%")
print(f"Total Conversions:   {df['conversions'].sum():,}")

main_only = main_df.groupby(['platform', 'model_type']).agg(avg_ctr=('ctr','mean')).reset_index()
best = main_only.loc[main_only['avg_ctr'].idxmax()]
print(f"\nBest performer:      {model_labels[best['model_type']]} on {best['platform']} (avg CTR {best['avg_ctr']:.2f}%)")
print("=" * 55)
