import json
import random
import time

import streamlit as st  # Streamlitライブラリをインポート
from func import password_generator, uuid_generator


def uuid_generator_app():
    # タイトルを設定
    st.title("UUID生成アプリ")
    # ユーザーからの入力を受け取る
    num_uuids = st.number_input(
        "生成するUUIDの数を入力してください", min_value=1, max_value=100, value=50
    )

    # ボタンを作成
    if st.button("UUIDを生成する"):
        # UUIDを生成
        uuids = uuid_generator(num_uuids)
        # UUIDを表示
        for uuid in uuids:
            st.write(uuid)


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


# BMI計算アプリ
def bmi_calculator_app():
    st.title("BMI計算アプリ")
    weight = st.number_input("体重(kg)", min_value=0.0, step=0.1)
    height = st.number_input("身長(cm)", min_value=0.0, step=0.1)
    if st.button("計算"):
        height_m = height / 100
        bmi = weight / (height_m**2)
        st.write(f"あなたのBMIは{bmi:.2f}です。")


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


# サイドバーでアプリを選択
st.sidebar.title("アプリ切り替え")
app_pages = {
    "UUID生成": uuid_generator_app,
    "パスワード生成": password_generator_app,
    "ストップウォッチ": stopwatch_app,
    "BMI計算": bmi_calculator_app,
    "HTTPステータスコードクイズ": http_status_code_quiz_app,
}

# サイドバーにリンク形式でページを表示
selection = st.sidebar.markdown("### アプリを選択してください:")
for page_name in app_pages.keys():
    if st.sidebar.button(page_name):
        st.session_state["current_page"] = page_name

# 現在のページを保持
if "current_page" not in st.session_state:
    st.session_state["current_page"] = list(app_pages.keys())[0]

# 選択されたアプリを実行
app_pages[st.session_state["current_page"]]()
