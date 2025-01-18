import streamlit as st
from func import uuid_generator

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
