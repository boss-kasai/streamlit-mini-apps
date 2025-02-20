import math
import re

import streamlit as st


def password_strength_check(password: str) -> int:
    """パスワードの強度を測定する関数"""
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score


def password_entropy(password: str) -> float:
    """パスワードのエントロピーを計算する関数"""
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32
    if charset_size == 0:
        return 0
    return len(password) * math.log2(charset_size)


def password_strength_check_app():
    st.title("パスワードの強度チェック")

    password = st.text_input("パスワードを入力してください", type="password")

    if st.button("強度をチェック"):
        entropy = password_entropy(password)
        st.write(f"パスワードのエントロピー: {entropy:.2f} bits")

        if entropy >= 128:
            st.success("最強")
        elif entropy >= 60:
            st.success("強")
        elif entropy >= 40:
            st.warning("中")
        else:
            st.error("弱")
