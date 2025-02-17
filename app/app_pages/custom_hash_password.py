import hashlib

import streamlit as st  # Streamlitライブラリをインポート


def custom_hash_password_app():
    st.title("カスタムハッシュパスワード生成")

    def hash_text(text: str, number: int, length: int, hash_method: str) -> str:
        """アルファベットと数字を結合してハッシュ化し、指定の長さの文字列を生成"""
        combined_text = text + str(number)
        if hash_method == "SHA-256":
            hash_value = hashlib.sha256(combined_text.encode()).hexdigest()
        elif hash_method == "SHA-1":
            hash_value = hashlib.sha1(combined_text.encode()).hexdigest()
        elif hash_method == "MD5":
            hash_value = hashlib.md5(combined_text.encode()).hexdigest()
        else:
            raise ValueError("サポートされていないハッシュ方式です")
        return hash_value[:length]  # パスワードの文字数に合わせて切り取る

    # ユーザー入力
    alphabet = st.text_input("アルファベット（例: abc）", max_chars=10)
    number = st.number_input("数字（1〜9999）", min_value=1, max_value=9999, step=1)
    password_length = st.number_input(
        "パスワードの文字数", min_value=1, max_value=64, step=1
    )
    hash_method = st.selectbox(
        "ハッシュ方式を選択してください", ["SHA-256", "SHA-1", "MD5"]
    )

    # ボタンを押したら処理を実行
    if st.button("パスワード生成", key="generate_password"):
        if alphabet and number and password_length:
            hashed_password = hash_text(alphabet, number, password_length, hash_method)
            st.success(f"生成されたパスワード: {hashed_password}")
        else:
            st.error("すべての項目を入力してください。")
