import streamlit as st  # Streamlitライブラリをインポート


# BMI計算アプリ
def bmi_calculator_app():
    st.title("BMI計算アプリ")
    weight = st.number_input("体重(kg)", min_value=0.0, step=0.1)
    height = st.number_input("身長(cm)", min_value=0.0, step=0.1)
    if st.button("計算"):
        height_m = height / 100
        bmi = weight / (height_m**2)
        st.write(f"あなたのBMIは{bmi:.2f}です。")
