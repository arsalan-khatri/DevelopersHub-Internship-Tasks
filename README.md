# AI/ML Engineering - Advanced Internship Tasks.

This repository contains the advanced projects completed during my AI/ML Engineering internship at Developers Hub Corporation. These tasks cover various domains including Transformer models, ML Pipelines, and Large Language Model (LLM) applications.

---

## Task 1: News Topic Classifier Using BERT

### Objective
Fine-tune a transformer model to classify news headlines into four distinct categories: World, Sports, Business, and Sci/Tech.

### Methodology
* **Dataset:** AG News Dataset from Hugging Face.
* **Model:** Fine-tuned the `bert-base-uncased` model using Hugging Face Transformers.
* **Preprocessing:** Implemented tokenization and text cleaning.
* **Evaluation:** Performance measured using Accuracy and F1-score.
* **Deployment:** Deployed for live interaction using a web interface.

### Skills Gained
* NLP using Transformers.
* Transfer learning and fine-tuning.
* Evaluation metrics for text classification.

---

## Task 2: End-to-End ML Pipeline with Scikit-learn

### Objective
Build a reusable and production-ready machine learning pipeline for predicting customer churn.

### Methodology
* **Dataset:** Telco Churn Dataset.
* **Pipeline API:** Implemented data preprocessing (scaling, encoding) using Scikit-learn Pipeline.
* **Algorithms:** Trained models like Logistic Regression and Random Forest.
* **Optimization:** Used GridSearchCV for hyperparameter tuning.
* **Export:** Exported the complete pipeline using `joblib` for reusability.

### Skills Gained
* ML pipeline construction and production-readiness.
* Hyperparameter tuning with GridSearch.
* Model export and reusability.

---
# Task 3: Multimodal ML – Housing Price Prediction

### Objective
Predict housing prices by merging visual features from house images with structured tabular data (sqft, beds, baths) to create a more accurate regression model.

### Methodology
* **Framework**: Developed using **TensorFlow/Keras** and **Scikit-Learn** for deep learning and data preprocessing.
* **Image Processing**: Implemented a **Convolutional Neural Network (CNN)** to extract deep visual features from house photos.
* **Feature Fusion**: Combined extracted image embeddings with scaled tabular features using a **Late Fusion** technique (concatenation).



* **Regression Model**: Built a multimodal architecture with multiple Dense layers to predict continuous price values.
* **Evaluation**: Performance was measured using **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.
* **Optimization**: Specifically optimized for **CPU-based training** on low-end hardware using efficient data sampling (5,000 samples) and image resizing.

### Skills Gained
* **Multimodal Machine Learning**: Integrating diverse data sources (visual + numerical) into a single model.
* **Computer Vision**: Using CNNs for feature extraction from real-world real estate imagery.
* **Feature Engineering**: Data normalization, scaling, and feature concatenation.
* **Regression & Evaluation**: Tuning deep learning models for high-value price prediction.

---

### Final Results Summary
* **MAE**: $265,925.03
* **RMSE**: $363,520.58

## Task 4: Context-Aware Chatbot Using LangChain or RAG

### Objective
Build a conversational chatbot that can remember context and retrieve external information during conversations.

### Methodology
* **Framework:** Developed using LangChain and Retrieval-Augmented Generation (RAG).
* **Memory:** Implemented context memory for maintaining conversational history.
* **Retrieval:** Answers are retrieved from a vectorized document store.
* **Knowledge Base:** Uses a custom corpus (PDFs/Internal documents).
* **Deployment:** Deployed as an interactive app with Streamlit.

### Skills Gained
* Conversational AI development.
* Document embedding and vector search.
* Retrieval-Augmented Generation (RAG) and LLM integration.

---

## Submission Details
* **Organization:** Developers Hub Corporation.
* **Deadline:** 15th February, 2026.
* **Requirements:** Jupyter Notebooks, Code Quality, and Detailed Documentation.
