# Task 2: End-to-End ML Pipeline with Scikit-learn Pipeline API

This project focuses on building a production-ready Machine Learning pipeline to predict customer churn. The goal is to create a reusable system that handles everything from raw data preprocessing to model prediction in a single workflow.

## Objective
The main objective of this task is to predict whether a customer will leave a service (Churn) based on their usage patterns and demographic data using the Telco Churn Dataset.

## Project Overview
In real-world AI applications, data is often messy. This project uses the Scikit-learn `Pipeline` API to automate the cleaning and transformation process, ensuring that the model remains consistent during both training and testing.

## Methodology

### 1. Data Preprocessing
Using the Pipeline API, the following steps were automated:
* **Handling Missing Values:** Cleaning null or empty records in the dataset.
* **Feature Scaling:** Normalizing numerical data (like monthly charges and tenure) to a standard scale.
* **Categorical Encoding:** Converting text-based data (like gender or contract type) into numerical format using One-Hot Encoding or Label Encoding.

### 2. Model Development
Two powerful algorithms were trained and compared:
* **Logistic Regression:** Used as a baseline model for binary classification.
* **Random Forest Classifier:** Used to capture complex patterns and improve prediction accuracy.

### 3. Hyperparameter Tuning
To get the best possible results, **GridSearchCV** was implemented. This allowed the system to automatically test different combinations of model parameters (like the number of trees in a forest) to find the most accurate version.

### 4. Model Export
The final, optimized pipeline was exported using the **joblib** library. This creates a serialized file that can be loaded into any production environment to make real-time predictions without rewriting the preprocessing code.

## Technologies Used
* **Python:** Core programming language.
* **Scikit-learn:** For the Pipeline API, model training, and GridSearchCV.
* **Pandas & NumPy:** For data manipulation.
* **Joblib:** For saving and exporting the final model.

## Key Results
* **Accuracy:** Successfully identified key factors leading to customer churn.
* **Reusability:** The final pipeline is fully modular, meaning it can handle new data instantly.
* **Production-Ready:** The exported `.joblib` file is ready for deployment in web or cloud applications.

## How to Run
1. Ensure you have the dependencies installed: `pip install scikit-learn pandas numpy joblib`.
2. Run the Jupyter Notebook to train the model and generate the pipeline file.
3. Use the exported model for making predictions on new customer data.
