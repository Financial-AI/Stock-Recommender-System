# Personalized Stock Recommender System

Personalized Stock Recommender System based on user interest toward company domain.

## Project Proposal

As more people work in the United States, more jobs are having pension removed from the benefits, which means less people will have a steady income when they retire when they are older. An alternative option is to start thinking about investing when people are young, such as stock investing, make good investment decisions, so when they are older, they will have a higher chance of having their savings grow exponentially. Similar to how netflix will gamify selecting movies using personalized recommendation, our goal will be to do the same for stock, presenting people with good stock investment choices based on the industry domain they are interested in. Therefore, when James opens his stock investing app, he will see rows of top stocks to invest in with each row indicating a field of healthcare and each cell within a row being a healthcare company. Ultimately, by gamifying stock investing with a netflix feel, we hope to encourage more people to start learning about stock investing early and make smart investments by the top recommendations based on the industry domain they are interested. Therefore, hopefully there will be more people who can retire from work with a good amount of savings.

> QUESTION: Do we include a Rasa Personalized Stock Recommendation Chatbot within app?

> NOTE: Imagine building this app for the Apple Vision Pro...


## CMPE 256 Project Submission Checklist

> NOTE: Going with submission format similar to CMPE 258 DL

> NOTE: Out of the tasks, I am most interested in creating a recommender system using DL and tailoring the prep data pipeline for DL (NiFi to PyTorch to Unity).

> NOTE: we wont need all these tasks to cover, we'll keep the ones we want to do

- [ ] 1. Team Dev Tasks
    - [ ] Content-based Filtering
    - [ ] Collaborative Filtering
        - [ ] Item-based CF
        - [ ] User-based CF
            - [ ] Vector Similarity
                - [ ] Cosine Similarity
                - [ ] Pearson Coefficient
                - [ ] Adjusted Cosine Similarity
            - [ ] Prediction
                - [ ] Simple Average
                - [ ] Weighted Average
                - [ ] Mean Centered Average
    - [ ] ML Models?
        - [ ] Supervised Learning:
            - [ ] Linear Regression
            - [ ] Gradient Boosted Decision Trees
            - [ ] Random Forests
        - [ ] Unsupervised Learning:
            - MF: Singular Value Decomposition (SVD)
            - MF: Latent Dirichlet Allocation (LDA)
            - Association Rules
            - Clustering
    - [ ] DL Models
        - [ ] Unsupervised Learning:
            - [ ] Restricted Boltzmann Machines
        - [ ] Supervised Learning:
            - [ ] CNN
            - [ ] RNN
            - [ ] LSTM
            - [ ] GRU
            - [ ] Transformers
            - [ ] LLMs
    - [ ] DRL Models
        - [ ] Markov Decision Process - Markov Chains
        - [ ] Actor-Critic Methods
        - [ ] Q-Learning
        - [ ] Policy Gradient Theorem
        - [ ] Proximal Policy Optimization (PPO)
    - [ ] Unity App
    - [ ] Rasa Chatbot?



- [ ] 4\. Ten minutes presentation and program demo:

    - [ ] (4.1) PPT (up to 5-7 slides) for 5-7 minutes presentation;
    - [ ] (4.2) Demo, 1 minute;
    - [ ] (4.3) Code walk-through for 1-2 minutes;
    - [ ] (4.4) Q&A, 1 minute.

- [ ] 5\. Save up to 20 ~ 50 seconds demo video into a file for submission.
- [ ] 6. Submit:

    - [ ] a. Executive Summary;
    - [ ] b. PPT;
    - [ ] c. Your saved video clip;
    - [ ] d. The program package (source code and all relevant files and folders);
    - [ ] e. A readme file. Be sure detailed adequate information is provided for testing and verification purpose.

- [ ] 7. Put all the above files into one file and zip it.
- [ ] 8. Use the following file naming convention for your zip file:

    - [ ] firstNamePerson1_firstNamePerson2_FirstNamePerson3_FirstNamePerson4_CoordinatorSID(last-4-digits)_cmpe258_team.zip.
    - [ ] Ex: `James_Guzman_Josef_Bustamante_Anshul_Shandilya_6649_cmpe256_team.zip`

- [ ] Submit it to the class canvas.

## Outline

- AI/ML Concepts
- Software Dependencies
- Setup Software Dev Environment
- How to Run Unity Personalized Stock Recommendation Demo
- How to Run Python Personalized Stock Recommendation Demo
    - Run Python Training Script
    - Run Python Deploy Script
- How to Run Apache NiFi
- Data Exploration
- DL Pipeline

## AI/ML Concepts

- Dataset
- ML models with Torch Tensors
- DL models
- DRL models


## Software Dependencies

Here are some of the software dependencies:

- Does H2O.ai's **H2O-3** include Rec Sys models?

- **H2O.ai's LLM Studio** for personalized Stock Recommendation?
- **Apache NiFi 2.0 Snapshot (custom Python Processors)**
- **Torch 2.0.1 (Needed for Rasa Actions Server)**
- **Unity 2021.3.13f**


- Rasa 3.2.4 (Rasa Chatbot Server) ?
- Rasa SDK 3.2.2 (Rasa Actions Server) ?
    - GPT based conversational AI vs rasa's other AI models...

- OpenCV-Python 4.6.0.66 (Needed for Rasa Actions Server)

- Seaborn 0.11.2
- Matplotlib 3.3.4
- Jupyter 1.0.0

Provide yml file of conda environment

## DL NiFi Pipeline

What processors are needed?

How should we go about visualizing the data?

