# streamlit-mini-apps

Streamlitで作成されたミニアプリ集。

1. UUID生成アプリ
2. パスワード生成アプリ
3. ストップウォッチアプリ

## 開発環境について

```bash
mkdir app test development
```

```bash
# 仮想環境の作成
python3.13 -m venv development/venv

# 仮想環境の有効化
source development/venv/bin/activate

# 依存関係のインストール
pip install -r ./app/requirements.txt

# 依存関係の保存
pip freeze > ./app/requirements.txt

```

## アプリケーションの実行

```bash
streamlit run app/main.py
```
