import uuid

from app.func import uuid_generator


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
