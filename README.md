# Ad Creative A/B Test Analysis
### Asan Doers Startup Competition — Performance Marketing Campaign (2024)

---

## Project Overview

This project analyzes the performance of paid social media campaigns using A/B testing across Facebook and TikTok. The goal is to identify which creative strategies drive higher click-through rates and engagement.

- **Total budget:** ₩300,000 KRW (~$230 USD)
- **Duration:** 4 weeks
- **Platforms:** Facebook Ads, TikTok Ads
- **Creatives tested:** 4 video ads across 2 experiments
- **Overall conversion rate:** TikTok 4.3% / Facebook 2.1% (ad click → website action)

---

## Experiment Structure

### Main Experiment: Influencer vs General Person
> **Does using an influencer's face vs. a general person's face produce higher CTR and conversion rate?**

Our service connects influencers and fans through 1:1 video calls. Two competing hypotheses:
- **Influencer close-up** → fans recognize the face → stronger emotional pull → higher CTR
- **General person close-up** → "someone like me" → relatability → lower barrier to click

To isolate the variable, both creatives used the same **close-up framing**.

| Creative | Model Type |
|---|---|
| Influencer Close-Up | Influencer |
| General Close-Up | General Person |

---

### Additional Experiment: Close-Up vs Full-Shot (Framing Effect)
> **Does showing only the face (close-up) vs. the full body affect performance?**

Close-up emphasizes facial expression and eye contact. Full-shot shows more context and style. We tested both across influencer and general creatives.

| Creative | Framing |
|---|---|
| Influencer Close-Up | Close-Up |
| Influencer Full-Shot | Full-Shot |
| General Close-Up | Close-Up |
| General Full-Shot | Full-Shot |

---

## Key Findings

### 1. Influencer close-up drove higher CTR across both platforms
- Facebook: Influencer avg **2.80%** vs General **1.94%**
- TikTok: Influencer avg **1.41%** vs General **1.40%**

> **Insight:** On Facebook, fans responded more strongly to recognizable influencer faces — consistent with the hypothesis that recognition drives clicks in a fan-platform context. The gap was smaller on TikTok, likely because TikTok's algorithm surfaces content based on behavior rather than brand recognition.

![](figures/fig1_main_experiment.png)

### 2. Budget reallocation improved CTR in Week 3–4
After Week 2 results confirmed influencer creatives were outperforming, budget was shifted toward the top-performing ads. CTR for influencer creatives rose further in Week 3 while general creative spend was reduced.

![](figures/fig2_weekly_trend.png)

### 3. Close-up consistently outperformed full-shot
- Facebook: Close-up avg CTR **2.32%** vs Full-shot **1.76%**
- TikTok: Close-up avg CTR **1.31%** vs Full-shot **1.19%**

> **Insight:** In short-form ad formats, direct eye contact and facial close-ups capture attention faster than full-body shots. This is consistent with findings in visual attention research suggesting faces — especially eyes — are processed first.

![](figures/fig3_framing_experiment.png)

### 4. Platform behavior differed
- **Facebook** drove higher CTR overall and showed a larger gap between influencer and general creatives
- **TikTok** showed higher conversion rates (TikTok **4.3%** vs Facebook **2.1%**) despite lower CTR — users who clicked on TikTok were more likely to take action on the landing page

> **Recommendation:** For an influencer-fan platform in early stages, prioritize influencer close-up creatives and allocate more budget to Facebook for CTR efficiency. Use TikTok for conversion-focused campaigns targeting warmer audiences.

![](figures/fig4_summary_heatmap.png)

---

## Tools Used

- **Python** — pandas, matplotlib, seaborn, numpy
- **Platforms** — Facebook Ads Manager, TikTok Ads

---

## Files

```
├── README.md
├── analysis.py
├── campaign_data.csv
└── figures/
    ├── fig1_main_experiment.png
    ├── fig2_weekly_trend.png
    ├── fig3_framing_experiment.png
    └── fig4_summary_heatmap.png
```

---

## Reflection

This project highlights that the most valuable part of data analysis is not only visualization, but the ability to ask the right questions and design meaningful experiments. Framing a clear hypothesis (influencer vs. general) forced me to design the experiment deliberately rather than just running ads and hoping something worked. The weekly trend analysis also showed me how iterative decision-making — adjusting budget based on mid-campaign data — is more effective than a set-and-forget approach. 
