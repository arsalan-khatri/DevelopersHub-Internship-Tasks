# Task 1: News Topic Classifier Using BERT.

This project focuses on building an AI model to automatically classify news headlines into four distinct categories using Natural Language Processing (NLP) and Deep Learning.

## Objective
The goal of this task is to fine-tune a pre-trained Transformer model (DistilBERT) to categorize news text into the following topics:
* **World**
* **Sports**
* **Business**
* **Sci/Tech**

## Project Overview
Instead of building a model from scratch, this project uses **Transfer Learning**. We take a pre-trained model (`distilbert-base-uncased`) that already understands English and fine-tune it specifically on news data to achieve high accuracy with less training time.

## Methodology

### 1. Dataset Selection
* **Source:** AG News Dataset (via Hugging Face Datasets).
* **Content:** Thousands of news headlines labeled into 4 categories.

### 2. Preprocessing & Tokenization
* Used the `AutoTokenizer` from the Transformers library.
* Text was converted into numerical format (tokens) with a maximum length of 128 tokens.
* Implemented padding and truncation to ensure consistent input size for the model.

### 3. Model Training
* **Architecture:** DistilBERT (A lighter, faster, and more memory-efficient version of BERT).
* **Hardware Optimization:** The training process was configured to run on CPU with a batch size of 8 to ensure stability on local machines.
* **Epochs:** Trained for 3 full passes (epochs) over the dataset.

### 4. Evaluation Metrics
The model was evaluated based on:
* **Accuracy:** How many headlines were correctly classified.
* **F1-Score:** The balance between precision and recall for all 4 categories.

## Key Results
* **Final Accuracy:** ~89.35%
* **Final F1-Score:** ~0.89
* **Training Loss:** Successfully reduced from 0.44 in the first epoch to 0.16 in the final epoch.

## Technologies Used
* **Python:** Core language.
* **Hugging Face Transformers:** For the DistilBERT model and Trainer API.
* **PyTorch:** Backend deep learning framework.
* **Gradio:** For deploying the web interface.
* **Scikit-learn:** For calculating evaluation metrics.

## How to Run
1. Install dependencies: `pip install transformers datasets torch scikit-learn gradio`.
2. Run the Jupyter Notebook `News_Topic_Classifier_Using_BERT.ipynb` to train/load the model.
3. Run `python app.py` to launch the interactive web interface where you can type headlines and see predictions.
