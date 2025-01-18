import uuid


# UUID生成アプリ
def uuid_generator(create_num):
    uuid_list = []  # UUIDを格納するリスト
    for _ in range(create_num):
        # UUIDを生成
        uuid_list.append(uuid.uuid4())
    return uuid_list
