import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('ridge_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')
default_values = joblib.load('default_values.pkl')
quality_map = joblib.load('quality_map.pkl')
categorical_cols = joblib.load('categorical_cols.pkl')
cat_options = joblib.load('cat_options.pkl')

st.title("🏠 توقع سعر البيت")
st.write("أدخل بيانات البيت عشان نتوقع سعره")

overall_qual = st.slider("الجودة العامة (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("مساحة المعيشة (قدم مربع)", min_value=0, value=1500)
garage_cars = st.slider("سعة الجراج (عدد العربيات)", 0, 4, 1)
total_bsmt_sf = st.number_input("مساحة البدروم (قدم مربع)", min_value=0, value=800)
year_built = st.number_input("سنة البناء", min_value=1870, max_value=2024, value=2000)
full_bath = st.slider("عدد الحمامات الكاملة", 0, 4, 2)
neighborhood = st.selectbox(
    "الحي",
    cat_options.get('Neighborhood', ['NAmes'])
)

if st.button("توقع السعر"):

    input_data = default_values.copy()

    input_data['OverallQual'] = overall_qual
    input_data['GrLivArea'] = gr_liv_area
    input_data['GarageCars'] = garage_cars
    input_data['TotalBsmtSF'] = total_bsmt_sf
    input_data['YearBuilt'] = year_built
    input_data['FullBath'] = full_bath

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    pred_log = model.predict(input_df)[0]
    pred_price = np.expm1(pred_log)

    st.success(f"السعر المتوقع: ${pred_price:,.0f}")
