import random

import streamlit as st  # Streamlitライブラリをインポート


def addition_trainer_app():
    st.title("足し算トレーニング")

    # セッション変数がなければ初期化
    if "x" not in st.session_state:
        st.session_state.x = 0
    if "y" not in st.session_state:
        st.session_state.y = 0
    if "z" not in st.session_state:
        st.session_state.z = 0
    if "operator" not in st.session_state:
        st.session_state.operator = "+"
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 0

    def generate_new_problem():
        """足し算または引き算の新しい問題を作成"""
        op = random.choice(["+", "-"])  # '+' か '-' のどちらかを選ぶ
        x = random.randint(1, 20)
        y = random.randint(1, 20)

        if op == "+":
            z = x + y
        else:
            # 引き算の場合は答えがマイナスにならないよう調整
            if y > x:
                x, y = y, x
            z = x - y

        st.session_state.x = x
        st.session_state.y = y
        st.session_state.z = z
        st.session_state.operator = op

    # ページ初回読み込み時、問題を生成
    if st.session_state.x == 0 and st.session_state.y == 0:
        generate_new_problem()

    st.markdown(
        "<h1 style='text-align: center; font-size: 60px;'>けいさんれんしゅう</h1>",
        unsafe_allow_html=True,
    )
    st.write(" ")

    # 大きめの文字で問題を表示
    question_text = f"<span style='font-size: 48px;'>{st.session_state.x} {st.session_state.operator} ? = {st.session_state.z}</span>"
    st.markdown(question_text, unsafe_allow_html=True)

    # ユーザーに答えを入力してもらう
    answer = st.text_input(
        "こたえを入れてね", value="", key="answer", label_visibility="collapsed"
    )

    # チェックボタン
    if st.button("チェック"):
        if answer.isdigit() or (answer.startswith("-") and answer[1:].isdigit()):
            # ユーザー入力を整数に変換
            ans_num = int(answer)

            # 正解か判定
            if ans_num == st.session_state.y:
                st.success("せいかい！")
                st.session_state.score += 1
            else:
                st.error(f"ちがうよ... せいかいは {st.session_state.y} だよ。")
            st.session_state.total_questions += 1
        else:
            st.warning("数字を入力してね。")

    st.write(" ")

    # 次の問題ボタン
    if st.button("つぎのもんだい"):
        # 入力欄クリアのために再度問題を生成
        generate_new_problem()
        # クエリパラメータを設定してページをリロード
        # st.query_params = {"rerun": "true"}

    # スコア表示
    st.write(f"スコア: {st.session_state.score} / {st.session_state.total_questions}")
