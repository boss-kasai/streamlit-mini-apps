import streamlit as st  # Streamlitライブラリをインポート

from app.functions.func import password_generator


def password_generator_app():
    # タイトルを設定
    st.title("パスワード生成アプリ")
    # ユーザーからの入力を受け取る
    password_length = st.number_input(
        "パスワードの長さを入力してください", min_value=1, max_value=1000, value=12
    )
    group_length = st.number_input(
        "何文字ごとに区切るかを入力してください", min_value=0, max_value=100, value=4
    )
    include_lowercase = st.checkbox("小文字を含む")
    include_uppercase = st.checkbox("大文字を含む")
    include_digits = st.checkbox("数字を含む")
    include_special = st.checkbox("特殊文字を含む")
    include_hiraganas = st.checkbox("ひらがなを含む")
    include_katakanas = st.checkbox("カタカナを含む")

    # ボタンを作成
    if st.button("パスワードを生成する"):
        # checkboxに1つもチェックが入っていない場合、エラーを表示
        if not any(
            [
                include_lowercase,
                include_uppercase,
                include_digits,
                include_special,
                include_hiraganas,
                include_katakanas,
            ]
        ):
            st.error("少なくとも1つのオプションを選択してください")
        else:
            # パスワードを生成
            passwords = password_generator(
                password_length,
                group_length,
                include_lowercase,
                include_uppercase,
                include_digits,
                include_special,
                include_hiraganas,
                include_katakanas,
            )
            # パスワードを表示
            for password in passwords:
                st.write(password)
