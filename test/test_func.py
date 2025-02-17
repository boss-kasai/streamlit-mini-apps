import string
import uuid

from app.functions.func import password_generator, uuid_generator


## UUID生成関数のテスト
# UUIDが作成されているか
def test_uuid_generator():
    # 関数の戻り値を取得
    result = uuid_generator(1)

    # 戻り値がUUIDのインスタンスであることを確認
    assert isinstance(result[0], uuid.UUID)


# 毎回違うUUIDが生成されるか
def test_uuid_generator_generates_unique_uuids():
    # UUIDを複数回生成
    uuid1 = uuid_generator(1)
    uuid2 = uuid_generator(1)

    # それぞれが異なることを確認
    assert uuid1 != uuid2


# 指定した個数のUUIDが生成されるか
def test_uuid_generator_generates_specified_number_of_uuids():
    # UUIDを生成
    uuids = uuid_generator(50)

    # 生成されたUUIDの個数が正しいことを確認
    assert len(uuids) == 50


## パスワード生成関数のテスト
def test_password_length_zero():
    """パスワード長が0の場合、適切なエラーメッセージを返す"""
    result = password_generator(0, 0, True, True, True, True, True, True)
    assert result == ["パスワードの長さを1以上にしてください"]


def test_no_options_selected():
    """いずれのオプションも選択されていない場合、適切なエラーメッセージを返す"""
    result = password_generator(10, 0, False, False, False, False, False, False)
    assert result == ["少なくとも1つのオプションを選択してください"]


def test_lowercase_only():
    """小文字のみを含むパスワードを生成する"""
    result = password_generator(10, 0, True, False, False, False, False, False)
    for password in result:
        assert all(c in string.ascii_lowercase for c in password)


def test_uppercase_only():
    """大文字のみを含むパスワードを生成する"""
    result = password_generator(10, 0, False, True, False, False, False, False)
    for password in result:
        assert all(c in string.ascii_uppercase for c in password)


def test_digits_only():
    """数字のみを含むパスワードを生成する"""
    result = password_generator(10, 0, False, False, True, False, False, False)
    for password in result:
        assert all(c in string.digits for c in password)


def test_special_only():
    """特殊文字のみを含むパスワードを生成する"""
    result = password_generator(10, 0, False, False, False, True, False, False)
    for password in result:
        assert all(c in string.punctuation for c in password)


def test_hiragana_only():
    """ひらがなのみを含むパスワードを生成する"""
    result = password_generator(10, 0, False, False, False, False, True, False)
    hiragana = "".join(chr(i) for i in range(0x3040, 0x30A0) if "ぁ" <= chr(i) <= "ん")
    for password in result:
        assert all(c in hiragana for c in password)


def test_katakana_only():
    """カタカナのみを含むパスワードを生成する"""
    result = password_generator(10, 0, False, False, False, False, False, True)
    katakana = "".join(
        chr(i)
        for i in range(0x30A0, 0x30FF + 1)
        if "ァ" <= chr(i) <= "ン" or "ー" == chr(i)
    )
    for password in result:
        assert all(c in katakana for c in password)


def test_mixed_characters():
    """複数のオプションを選択した場合のパスワードを生成する"""
    result = password_generator(10, 0, True, True, True, True, True, True)
    for password in result:
        assert any(c.islower() for c in password)  # 小文字
        assert any(c.isupper() for c in password)  # 大文字
        assert any(c.isdigit() for c in password)  # 数字
        assert any(c in string.punctuation for c in password)  # 特殊文字
        assert any("ぁ" <= c <= "ん" for c in password)  # ひらがな
        assert any("ァ" <= c <= "ン" or c == "ー" for c in password)  # カタカナ


def test_grouped_passwords():
    """指定されたグループ長でパスワードが区切られる"""
    result = password_generator(12, 4, True, True, False, False, False, False)
    for password in result:
        groups = password.split("-")
        assert all(len(group) == 4 for group in groups)


def test_randomness():
    """生成されるパスワードがランダムであることを確認"""
    for i in range(100):
        result1 = password_generator(10, 0, True, True, True, True, True, True)
        result2 = password_generator(10, 0, True, True, True, True, True, True)
        assert result1 != result2
