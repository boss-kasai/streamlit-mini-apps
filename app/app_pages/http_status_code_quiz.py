import json
import random

import streamlit as st  # Streamlitライブラリをインポート


def http_status_code_quiz_app():
    st.title("HTTP ステータスコード クイズ")

    # JSONファイルを開いて読み込む
    with open("app/data/httpStatusCode.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # JSONをPythonの辞書（dict）として読み込む

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = random.sample(data, 10)
        st.session_state.current_question = 0
        st.session_state.score = 0

    question = st.session_state.quiz_data[st.session_state.current_question]

    st.write(f"### 問 {st.session_state.current_question + 1} / 10")
    st.write("**ステータスコードの説明:**")
    st.info(question["description"])

    if "user_input" not in st.session_state:
        st.session_state.user_input = 0

    user_input = st.number_input(
        "このステータスコードは？",
        min_value=0,
        max_value=599,
        step=1,
        format="%d",
        value=st.session_state.user_input,
    )

    if "options" not in st.session_state:
        st.session_state.options = random.sample([q["message"] for q in data], 4)
        if question["message"] not in st.session_state.options:
            st.session_state.options[random.randint(0, 3)] = question["message"]

    selected_message = st.radio(
        "このステータスコードのメッセージを選んでください", st.session_state.options
    )

    if st.button("回答する"):
        correct_code = question["code"]
        correct_message = question["message"]

        if user_input == correct_code and selected_message == correct_message:
            st.success("正解！")
            st.session_state.score += 1
        else:
            st.error(f"不正解！正解は {correct_code} ({correct_message}) です。")

        st.session_state.current_question += 1
        st.session_state.user_input = 0  # デフォルト値に戻す
        if st.session_state.current_question >= 10:
            st.write("### クイズ終了 🎉")
            st.write(f"あなたの正解数: {st.session_state.score} / 10")
            st.session_state.current_question = 0
            st.session_state.quiz_data = random.sample(data, 10)
            st.session_state.score = 0
        else:
            if st.button("次の問題に進む"):
                st.experimental_rerun()
