# Developers Hub Corporation - AI/ML Engineering Internship Tasks

[cite_start]This repository contains the advanced internship tasks completed during my AI/ML Engineering internship at Developers Hub Corporation[cite: 1, 2]. [cite_start]The projects cover various domains including Natural Language Processing (NLP), Machine Learning Pipelines, and Large Language Model (LLM) applications[cite: 6, 7].

## Repository Link
https://github.com/arsalan-khatri/DevelopersHub-Internship-Tasks

---

## Task 1: News Topic Classifier Using BERT

### Objective
[cite_start]The primary goal of this task was to fine-tune a transformer model to accurately classify news headlines into four distinct categories: World, Sports, Business, and Science/Technology[cite: 10, 11, 12].

### Methodology
- [cite_start]**Model Selection:** Utilized the `bert-base-uncased` model from Hugging Face[cite: 17].
- [cite_start]**Dataset:** Employed the AG News dataset[cite: 14].
- [cite_start]**Preprocessing:** Performed tokenization and data cleaning using Hugging Face Transformers[cite: 16].
- [cite_start]**Fine-tuning:** Trained the model using transfer learning to adapt it to the specific news categories[cite: 17, 22].
- [cite_start]**Deployment:** The model is deployed for live interaction[cite: 19].

### Key Results
- [cite_start]Achieved high performance measured via Accuracy and F1-score[cite: 18].
- [cite_start]Successfully demonstrated lightweight model deployment for real-time text classification[cite: 24].

---

## Task 2: End-to-End ML Pipeline with Scikit-learn

### Objective
[cite_start]Built a production-ready and reusable machine learning pipeline designed to predict customer churn using the Telco Churn dataset[cite: 25, 26, 27, 29].

### Methodology
- [cite_start]**Pipeline Construction:** Integrated data preprocessing steps, including scaling and encoding, using the Scikit-learn Pipeline API[cite: 31].
- [cite_start]**Model Training:** Trained and compared Logistic Regression and Random Forest models[cite: 32].
- [cite_start]**Optimization:** Used GridSearchCV for exhaustive hyperparameter tuning to find the best model configuration[cite: 33].
- [cite_start]**Model Export:** Exported the final trained pipeline using `joblib` for future reusability in production environments[cite: 34, 38].

### Key Results
- [cite_start]Developed a modular code structure that allows for easy maintenance and scalability[cite: 36, 39].

---

## Task 4: Context-Aware Chatbot Using LangChain (RAG)

### Objective
[cite_start]Developed a conversational AI assistant capable of maintaining chat history and retrieving information from external documents to provide contextually accurate responses[cite: 55, 56, 57].

### Methodology
- [cite_start]**Framework:** Built using LangChain and Retrieval-Augmented Generation (RAG) architecture[cite: 55, 61].
- [cite_start]**Document Processing:** Implemented document embedding and storage in a vectorized document store[cite: 63, 67].
- [cite_start]**Context Management:** Integrated conversation history memory to allow the chatbot to remember previous user inputs[cite: 62].
- [cite_start]**Retrieval:** Engineered a system to fetch relevant information from a custom knowledge base before generating responses[cite: 63, 68].
- [cite_start]**Deployment:** Developed a user interface using Streamlit for easy accessibility[cite: 64].

### Key Results
- [cite_start]Successfully integrated LLMs with external data sources[cite: 69].
- [cite_start]Created a seamless conversational experience with persistent context[cite: 66].

---

## Submission Requirements
Each task includes:
- [cite_start]Jupyter Notebooks with documented code and logic[cite: 86, 94].
- [cite_start]Clear explanations of data preprocessing and model development[cite: 88, 89].
- [cite_start]Evaluation metrics and visualizations[cite: 90, 91].
