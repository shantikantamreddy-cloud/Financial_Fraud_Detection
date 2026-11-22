
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

st.title("Financial Fraud Detection System")
st.write("Upload transaction data to detect possible fraud.")

uploaded_file = st.file_uploader(
    "Upload transaction CSV",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Transactions")
        st.dataframe(data.head())

        if st.button("Detect Fraud"):
            expected_features = list(model.feature_names_in_)

            missing = [
                col for col in expected_features
                if col not in data.columns
            ]

            if missing:
                st.error(f"Missing columns: {missing}")

            else:
                X = data[expected_features]
                predictions = model.predict(X)

                results = data.copy()

                results["Prediction"] = [
                    "Fraudulent" if p == 1 else "Genuine"
                    for p in predictions
                ]

                st.subheader("Prediction Results")
                st.dataframe(results)

                fraud_count = sum(predictions == 1)

                st.write(
                    "Fraud transactions detected:",
                    fraud_count
                )

                st.download_button(
                    label="Download Results",
                    data=results.to_csv(index=False),
                    file_name="fraud_predictions.csv",
                    mime="text/csv"
                )

    except Exception as e:
        st.error(f"Prediction error: {e}")
