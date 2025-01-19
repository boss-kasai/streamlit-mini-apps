import random
import string
import uuid


# UUID生成関数
def uuid_generator(create_num):
    uuid_list = []  # UUIDを格納するリスト
    for _ in range(create_num):
        # UUIDを生成
        uuid_list.append(uuid.uuid4())
    return uuid_list


# パスワード生成関数
def password_generator(
    password_length,
    group_length,
    include_lowercase,
    include_uppercase,
    include_digits,
    include_special,
    include_hiraganas,
    include_katakanas,
):
    if password_length == 0:
        return ["パスワードの長さを1以上にしてください"]
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
        return ["少なくとも1つのオプションを選択してください"]
    # パスワードに使用する文字を定義
    characters = ""
    if include_lowercase:  # 小文字を含む
        characters = string.ascii_lowercase
    if include_uppercase:  # 大文字を含む
        characters += string.ascii_uppercase
    if include_digits:  # 数字を含む
        characters += string.digits
    if include_special:  # 特殊文字を含む
        characters += string.punctuation
    if include_hiraganas:  # ひらがなを含む
        # ひらがな一覧を取得
        hiragana = "".join(
            chr(i) for i in range(0x3040, 0x30A0) if "ぁ" <= chr(i) <= "ん"
        )
        characters += hiragana
    if include_katakanas:  # カタカナを含む
        # 基本カタカナ一覧を取得
        katakana = "".join(
            chr(i)
            for i in range(0x30A0, 0x30FF + 1)
            if "ァ" <= chr(i) <= "ン" or "ー" == chr(i)
        )
        characters += katakana

    passwords = []
    while len(passwords) < 50:
        password = "".join(random.choices(characters, k=password_length))
        if include_lowercase:
            # 小文字が含まれていない場合、処理をスキップ
            if not any(c.islower() for c in password):
                continue
        if include_uppercase:
            # 大文字が含まれていない場合、処理をスキップ
            if not any(c.isupper() for c in password):
                continue
        if include_digits:
            # 数字が含まれていない場合、処理をスキップ
            if not any(c.isdigit() for c in password):
                continue
        if include_special:
            # 特殊文字が含まれていない場合、処理をスキップ
            if not any(c in string.punctuation for c in password):
                continue
        if include_hiraganas:
            # ひらがなが含まれていない場合、処理をスキップ
            if not any(c in hiragana for c in password):
                continue
        if include_katakanas:
            # カタカナが含まれていない場合、処理をスキップ
            if not any(c in katakana for c in password):
                continue
        # 指定文字数ごとに区切る
        if group_length == 0:
            passwords.append(password)
            continue
        else:
            grouped_password = "-".join(
                [
                    password[i : i + group_length]
                    for i in range(0, len(password), group_length)
                ]
            )
            passwords.append(grouped_password)

    return passwords
