import time

import streamlit as st


def pomodoro_timer_app():
    st.title("ポモドーロタイマー")

    work_minutes = st.number_input("作業時間 (分)", min_value=1, max_value=60, value=25)
    break_minutes = st.number_input("休憩時間 (分)", min_value=1, max_value=60, value=5)

    if st.button("スタート"):
        st.write("作業時間スタート！")
        work_placeholder = st.empty()
        stop_button = st.button("ストップ", key="stop_button")
        for i in range(work_minutes * 60 + 1):
            if stop_button:
                st.write("タイマーが停止されました。")
                return
            work_placeholder.write(f"残り時間: {work_minutes * 60 - i} 秒")
            time.sleep(1)
        st.write("休憩時間スタート！")
        break_placeholder = st.empty()
        for i in range(break_minutes * 60 + 1):
            if stop_button:
                st.write("タイマーが停止されました。")
                return
            break_placeholder.write(f"残り時間: {break_minutes * 60 - i} 秒")
            time.sleep(1)
        st.write("ポモドーロサイクル完了！")
