# Multimodal House Price Prediction
### Predicting Real Estate Prices using Images and Tabular Data

This project implements a **Multimodal Machine Learning** model to predict housing prices. Unlike standard models that only use numbers, this model looks at both **house photos** and **structured features** (sqft, beds, baths) to make a more accurate prediction.

---

## Project Overview
In this task, we merged two different data types into one single Neural Network:
* **Tabular Branch:** Processes numerical data like square footage and room counts.
* **Image Branch (CNN):** Processes house images to extract visual features.
* **Late Fusion:** Both branches are merged (concatenated) to predict the final price.



---

## Technical Implementation
This project is specifically optimized for **Low-End Laptops** without a GPU:
* **Optimized Sampling:** Used a subset of 5,000 samples to ensure stable CPU training.
* **Custom CNN:** A lightweight Convolutional Neural Network was built to save memory.
* **Image Preprocessing:** Images were resized to 100x100 and normalized by 255.0 for faster convergence.

---

## Project Structure
* `data_csv/`: Contains the `socal2.csv` dataset.
* `images/`: Contains house images named by their `image_id`.
* `task.ipynb`: The main Jupyter Notebook with the training code.

---

## Model Results
After training for 5 epochs with a batch size of 8, the model achieved the following results on the test set:

| Metric | Value |
| :--- | :--- |
| **Mean Absolute Error (MAE)** | $265,925.03 |
| **Root Mean Squared Error (RMSE)** | $363,520.58 |



---

## How to Run
1.  Clone this repository.
2.  Ensure your folder structure matches the **Project Structure** section above.
3.  Install dependencies: `pip install tensorflow pandas numpy matplotlib scikit-learn pillow tqdm`.
4.  Run the `task.ipynb` notebook.

---

## Sample Prediction
The model successfully predicts prices close to the actual value. For example:
* **Actual Price:** $749,999.00
* **Predicted Price:** $826,886.88
* **Accuracy:** Within ~10% error margin for high-value properties.
