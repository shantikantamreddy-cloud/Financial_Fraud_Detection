# Financial Fraud Detection Using Machine Learning

## Project Overview
This project uses Machine Learning to identify potentially fraudulent financial transactions. It compares Logistic Regression and Random Forest classification models and provides an interactive web application built using Streamlit.

## Objectives
- Analyze financial transaction data.
- Identify fraudulent and genuine transactions.
- Handle imbalanced classification data.
- Train and evaluate machine learning models.
- Build an interactive fraud detection application.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## Machine Learning Models
1. Logistic Regression
2. Random Forest Classifier

## Model Performance

Random Forest achieved the following results on the held-out test set:

| Metric | Score |
|---|---:|
| Precision (Fraud) | 0.94 |
| Recall (Fraud) | 0.89 |
| F1-score (Fraud) | 0.91 |

Note: The test set contained only 18 fraudulent transactions. Results should be interpreted cautiously and do not establish real-world production performance.

## Streamlit Application
The application allows users to:
- Upload transaction data in CSV format.
- Detect potentially fraudulent transactions.
- View prediction results.
- Download prediction results as a CSV file.

## Project Files
- `Financial_Fraud_Detection.ipynb` – Machine learning notebook.
- `app.py` – Streamlit application.
- `fraud_detection_model.pkl` – Trained Random Forest model.
- `requirements.txt` – Required Python libraries.
- `sample_transactions.csv` – Sample input transactions.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Dataset
Credit Card Fraud Detection dataset from Kaggle:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Author
Shanti Kantamreddy

## Disclaimer
This project is developed for educational and portfolio purposes. It is not intended for real-world financial decision-making without further validation.# Financial_Fraud_Detection
Financial Fraud Detection using Machine Learning and Streamlit
