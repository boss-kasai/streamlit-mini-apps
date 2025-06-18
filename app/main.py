import sys
from pathlib import Path

import streamlit as st  # Streamlitライブラリをインポート

sys.path.append(str(Path(__file__).resolve().parent.parent))  # プロジェクトルートを追加

from app_pages.addition_trainer import addition_trainer_app
from app_pages.bmi_calculator import bmi_calculator_app
from app_pages.custom_hash_password import custom_hash_password_app
from app_pages.date_calendar import date_calendar_app
from app_pages.http_status_code_quiz import http_status_code_quiz_app
from app_pages.password_generator import password_generator_app
from app_pages.password_strength_check import password_strength_check_app
from app_pages.pomodoro import pomodoro_timer_app
from app_pages.stopwatch import stopwatch_app
from app_pages.uuid_generator import uuid_generator_app


def home_app():
    st.title("Home")
    st.write("Streamlitで作成されたミニアプリ集へようこそ！")
    st.write("サイドバーからアプリを選択してください。")


# サイドバーでアプリを選択
st.sidebar.title("アプリ切り替え")
app_pages = {
    "Home": home_app,
    "UUID生成": uuid_generator_app,
    "パスワード生成": password_generator_app,
    "ストップウォッチ": stopwatch_app,
    "BMI計算": bmi_calculator_app,
    "HTTPステータスコードクイズ": http_status_code_quiz_app,
    "カスタムハッシュパスワード生成": custom_hash_password_app,
    "あの日まで何日？": date_calendar_app,
    "パスワードの強度チェック": password_strength_check_app,
    "算数練習(足し算)": addition_trainer_app,
    "ポモドーロタイマー": pomodoro_timer_app,
}

# サイドバーにリンク形式でページを表示
selection = st.sidebar.markdown("### アプリを選択してください:")
for page_name in app_pages.keys():
    if st.sidebar.button(page_name, key=page_name):
        st.session_state["current_page"] = page_name

# 現在のページを保持
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# 選択されたアプリを実行
app_pages[st.session_state["current_page"]]()
