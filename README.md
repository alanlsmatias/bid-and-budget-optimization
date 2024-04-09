# Bid and Budget optimization based on Cost Per Engagement (CPE)

## Usage
Install the dependencies and the bid-and-budget-optimizer package (the package is currently empty):
- `pip install .`
---
Install the dependencies and the bid-and-budget-optimizer package in develop model:
- `pip install -e .`
---
Additionally, For running the *Bid_And_Budget_Optimization* notebook, one must install some extra NLTK components.

## 1. The Bid and Budget optimization strategy
The strategy is straightforward: one model is trained to predict the *Media Spend* and another model is trained to predict the number of *Engagements*. Both models are Gaussian Processes (GP) trained considering the historical Bid, Budget and Audience. Afterwards, the Bid and Budget values are optimized through brute-force. Define $Y_s$ and $Y_e$ as the Media Spend and Engagements variables; the strategy steps are:
1. Train a GP, $\mathrm{GP}_s$, to predict the $\log Y_s$;
2. Train a second GP, $\mathrm{GP}_e$, to predict the $\log Y_e$;
3. Build the Bid and Budget grid;
4. For each item and its respective audience, predict the $\log Y_s$ ahd $\log Y_e$ for each combination of bid and budget;
5. Recover the original $Y_s \sim \exp\\{\log Y_s\\} = \mathrm{LogNormal}(\mu_s, \sigma_s^2)$;
6. Recover the original $Y_e \sim \exp\\{\log Y_e\\} = \mathrm{LogNormal}(\mu_e, \sigma_e^2)$;
7. Compute the expected CPE for each item, $CPE_i = \mathbb{E}[Y_{si}] / \mathbb{E}[Y_{ei}]$;
8. Obtain the $i$-th Bid and Budget based on the following objective: $i = \arg\min CPE_i\\:\\::\\:\\: budget_i \geq \mathbb{E}[Y_{si}]$.

## 2. Feature Engineering
The following features and its respectives transformations where used to train both $\mathrm{GP}_s$ and $\mathrm{GP}_e$:
- Numerical:
  - Variables: *bid, budget, active_days*.
  - Transform: $\mathrm{Log} \rightarrow \mathrm{StandardScaling}$.
- Categorical:
  - Variables: *item, group, channel, target_age, target_os, target_gender, content_category, content_sub_category*.
  - Transform: $\mathrm{OneHotEncoding}$.
- Text:
  - Variables: *healine, story_summary, target_interest, target_geo*.
  - Transform: $\mathrm{Tokenize} \rightarrow \mathrm{Stemmize} \rightarrow \mathrm{TF-IDF}$.
