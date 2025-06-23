from datetime import date

import streamlit as st


def calculate_interest_growth_app():
    """
    Streamlitアプリケーションのエントリーポイント。
    ユーザーからの入力を受け取り、金利計算を行う。
    """
    # アプリのタイトル

    st.title("金利計算アプリ")

    start_date = st.date_input("開始日を選んでください", date(2025, 2, 14))
    end_date = st.date_input("終了日（通常は今日）", date.today())
    principal = st.number_input("初期金額", min_value=0.0, value=1000.0)
    rate = st.number_input("利率（％）", min_value=0.0, value=10.0) / 100
    interval = st.number_input("利率適用間隔（日）", min_value=1, value=10)

    if st.button("計算する"):
        final_amount = calculate_interest_growth(
            start_date, end_date, principal, rate, interval
        )
        st.success(f"最終金額は {final_amount:,.2f} 円 です")


def calculate_interest_growth(
    start_date: date, end_date: date, principal: float, rate: float, interval_days: int
) -> float:
    """
    指定した期間・利率・適用間隔に基づいて金額を複利で計算する。

    Parameters:
    - start_date (date): 計算開始日
    - end_date (date): 計算終了日（通常は今日）
    - principal (float): 初期金額
    - rate (float): 利率（例: 0.02 は2%）
    - interval_days (int): 何日ごとに利率が適用されるか

    Returns:
    - float: 複利適用後の最終金額
    """
    days_diff = (end_date - start_date).days
    periods = days_diff // interval_days
    amount = principal

    for _ in range(periods):
        amount *= 1 + rate  # これは複利計算です。各期間ごとに利率が元本に乗算されます。

    return round(amount, 2)
