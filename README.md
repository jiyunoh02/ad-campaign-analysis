# 📊 Ad Creative A/B Test Analysis
### Asan Doers Startup Competition — Performance Marketing Campaign (2024)

---

## 🗂 Project Overview

As the **Performance Marketing Lead** for a startup competition team, I planned and executed a one-month paid advertising campaign across **Facebook and TikTok** with a total budget of ₩300,000 KRW (~$230 USD).

To maximize conversion efficiency, I designed an **A/B test across 6 distinct video creatives** varying subject type and framing, then used the results to reallocate budget toward top-performing ads.

This repository documents the data analysis I performed after the campaign to extract structured insights from the results.

---

## 🎯 Research Questions

1. Which creative concept drives the highest CTR?
2. Does **framing** (bust-only vs. full-body) affect performance?
3. Which platform performs better for **CTR** vs. **conversion rate**?
4. Does **video outperform photo** for the same creative concept?
5. How should budget be reallocated based on test results?

---

## 🧪 Creative Variables Tested

| Variable | Options Tested |
|---|---|
| **Subject Type** | Human face / AI-generated face / Animal character |
| **Framing** | Bust-only / Full-body |
| **Format** | Video / Photo (Facebook only) |
| **Platform** | Facebook / TikTok |

---

## 📈 Key Findings

### 1. Best Creative: Human Face, Bust-Only
- Achieved the highest CTR on Facebook (**2.78%**) — nearly 2x the campaign average
- Human faces consistently outperformed AI faces and character mascots across both platforms
- Bust-only framing outperformed full-body across all subject types and platforms

> **Insight:** Viewers respond more strongly to close-up human faces — likely because they create a sense of direct eye contact and emotional connection, which is critical in short-form ad formats.

### 2. Platform Differences: Facebook vs TikTok
- **Facebook** drove higher CTR overall (avg 1.77% vs 1.15%)
  - More effective for driving survey/form completions
- **TikTok** drove higher website conversion rate (avg 33.0% vs 25.0%)
  - Users who clicked on TikTok were more likely to take action on the landing page

> **Insight:** Facebook users were more likely to click; TikTok users who clicked were more likely to convert. Optimal strategy: use Facebook for awareness/engagement, TikTok for direct conversion campaigns.

### 3. Video vs Photo (Facebook)
- Video CTR (avg **2.36%**) outperformed Photo CTR (avg **1.52%**) for same concept
- Conversion rate also higher for video (**30.4%** vs **26.4%**)

> **Insight:** Even with a simple filming setup, video consistently outperformed static images — motion captures attention in the feed.

### 4. Budget Reallocation
Based on Week 1–2 test results, I reallocated **63% of remaining budget** to the top 2 creatives (Human Bust — Human and AI versions), which improved overall click volume while reducing wasted spend on underperforming concepts.

---

## 🛠 Tools Used

- **Python** — pandas, matplotlib, seaborn
- **Data Source** — Reconstructed from campaign records (Facebook Ads Manager / TikTok Ads)
- **Platforms** — Facebook Ads, TikTok Ads

---

## 📁 Files

```
├── README.md
├── campaign_data.csv        ← Per-creative performance data
├── analysis.py              ← Full analysis script
└── figures/
    ├── fig1_platform_comparison.png
    ├── fig2_ab_test_ctr.png
    ├── fig3_framing_effect.png
    ├── fig4_video_vs_photo.png
    └── fig5_budget_reallocation.png
```

---

## 💡 What I Learned

This project taught me that **data without interpretation is just numbers**. The real value came from asking *why* — why did bust-only outperform full-body? Why did TikTok convert better despite lower CTR? Translating those questions into testable hypotheses and actionable budget decisions is what performance analytics is actually about.

This experience is what motivated me to pursue a data analytics career path and transfer into Information Management.
