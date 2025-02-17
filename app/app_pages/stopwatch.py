import time

import streamlit as st  # Streamlitライブラリをインポート


def stopwatch_app():
    st.title("ストップウォッチ")

    # ストップウォッチの状態を保持するためのセッションステート
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "running" not in st.session_state:
        st.session_state.running = False
    if "elapsed_time" not in st.session_state:
        st.session_state.elapsed_time = 0.0

    # 開始ボタン
    if st.button("スタート"):
        if not st.session_state.running:
            st.session_state.start_time = time.time() - st.session_state.elapsed_time
            st.session_state.running = True

    # 停止ボタン
    if st.button("ストップ"):
        if st.session_state.running:
            st.session_state.elapsed_time = time.time() - st.session_state.start_time
            st.session_state.running = False

    # リセットボタン
    if st.button("リセット"):
        st.session_state.start_time = None
        st.session_state.running = False
        st.session_state.elapsed_time = 0.0

    # 時間表示のためのプレースホルダー
    time_display = st.empty()

    # ストップウォッチのカウント
    while st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        time_display.write(f"経過時間: {st.session_state.elapsed_time:.2f} 秒")
        time.sleep(0.01)  # 10ミリ秒ごとに更新
        st.rerun()

    # ストップウォッチが停止しているときの時間表示
    time_display.write(f"経過時間: {st.session_state.elapsed_time:.2f} 秒")
