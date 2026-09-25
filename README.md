# 🏠 House Price Prediction

A Machine Learning web application that predicts house prices based on selected property features.

## 🚀 Features

* Predict house prices using Machine Learning
* Interactive Streamlit web interface
* User inputs for:

  * Overall Quality
  * Living Area
  * Garage Capacity
  * Basement Area
  * Year Built
  * Full Bathrooms
  * Neighborhood

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## 🤖 Machine Learning Model

The project uses **Ridge Regression** to predict house prices.

The target price was transformed using `log1p` during model training, then converted back to the original price scale using `expm1` during prediction.

## ▶️ Run the App

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 📁 Project Files

* `app.py` → Streamlit application
* `ridge_model.pkl` → Trained Machine Learning model
* `feature_columns.pkl` → Features used by the model
* `default_values.pkl` → Default feature values
* `quality_map.pkl` → Quality mapping
* `categorical_cols.pkl` → Categorical columns
* `cat_options.pkl` → Categorical options
* `data_description.txt` → Dataset description
* `requirements.txt` → Required Python libraries
