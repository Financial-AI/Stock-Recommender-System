# Personalized Stock Recommender System

Personalized Stock Recommender System for offering recommendations toward stock investing and buying/selling stocks.

## Abstract

With many companies having pension plans removed from their job benefits [1] - [3], they transitioned to adopting contributory retirement plans like 401 (K) encouraging people to save, invest, and manage their own money for retirement [2]. However, many people still end up leaving their jobs financially unprepared for retirement [4], potentially resulting in them having no retirement savings [1] [3]. Even when people do have 401(K) accounts, it takes time for them to continually manage their portfolios. It takes time researching companies and industries to choose the right stocks. Even with funds, fund managers are prone to human error and human bias. Therefore, we are proposing an AI personalized recommender system toward stock investing that will be tailored for people’s industry domains of interest. The goal is to encourage people to learn about investing their money early into their career. It will also make it easier for people to start investing and potentially result in more people being prepared for retirement through retirement savings.

## CMPE 256 Project Submission Checklist

> NOTE: Going with submission format similar to CMPE 258 DL

> NOTE: Out of the tasks, I am most interested in creating a recommender system using DL and tailoring the prep data pipeline for DL (NiFi to PyTorch to Unity).

> NOTE: we wont need all these tasks to cover, we'll keep the ones we want to do

- [x] 1. Team Dev Tasks
    - [x] Content-based Filtering
        - [x] Stock Technical Indicators (MACD, GCD, RSI, Financial Status)
    - [x] DL Models
        - [x] Supervised Learning:
            - [x] PyTorch LSTM
            - [x] TensorFlow Keras Transformers
    - [x] Kaggle and GitHub Repos
        - [x] Jupyter Notebooks
    - [x] H2O Wave App
        - [x] Home Page Bootstrap Stock Recommender System
        - [x] EDA Telemetry Page Bootstrap Stock Graphs (Moving Average 100 vs Close Price, Closing Price Predictions used by Recommender System, etc)
        - [ ] Future Work: Train Model, Deploy Model

- [x] 2\. 15 minute presentation and program demo:

    - [x] (4.1) PPT (16 slides) for 12-15 minute presentation
    - [x] (4.2) Demo 1 minute.
    - [x] (4.4) Q&A, 1 minute.

- [x] 3\. Save up to 20 ~ 50 seconds demo video into a file for submission. Embedded in our presentation
- [x] 4\. Submit project to SJSU canvas:
    - [x] a. Project Report
        - GitHub repo and Dataset url included
    - [x] b. PPT

## Software Libraries

- **H2O.ai's Wave 1.0.0** for personalized Stock Recommendation fullstack
- **Torch 2.0.1**
- **TensorFlow 2.12.0**

## References

- [1] J. Sahadi, “Traditional pension plans are pretty rare. but here’s who still has them and how they work | CNN business,” CNN, https://www.cnn.com/2023/09/07/success/pensions-retirement-savings-explained/index.html (accessed Oct. 20, 2023).

- [2] J. Sabelhaus and A. H. Volz, “Are disappearing employer pensions contributing to rising wealth inequality?,” Federal Reserve, Board of Governors of the Federal Reserve System, https://www.federalreserve.gov/econres/notes/feds-notes/are-disappearing-employer-pensions-contributing-to-rising-wealth-inequality-20190201.html (accessed Oct. 20, 2023).

- [3] D. de Visé, “Nearly half of baby boomers have no retirement savings,” The Hill, https://thehill.com/business/personal-finance/3991136-nearly-half-of-baby-boomers-have-no-retirement-savings/ (accessed Oct. 20, 2023).

- [4] M. A. Z. Knoll, “Behavioral and Psychological Aspects of the Retirement Decision,” Social Security Administration Research, Statistics, and Policy Analysis, https://www.ssa.gov/policy/docs/ssb/v71n4/v71n4p15.html (accessed Oct. 20, 2023).

