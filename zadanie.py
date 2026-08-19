# def read_csv_to_dicts(filename: str) -> list[dict]:
#     result = []
#     with open(filename, mode='r', encoding='utf-8') as f:
#         lines = f.readlines()
#
#     headers = lines[0].strip().split(',')
#     for line in lines[1:]:
#
#         if not line.strip():
#             continue
#         values = line.strip().split(',')
#
#         row_dict = dict(zip(headers, values))
#         result.append(row_dict)
#
#     return result
#
#
# print(read_csv_to_dicts('C:\\Users\\vladu\\OneDrive\\Рабочий стол\\file.csv'))
#
#


class TestDataFactory:
    total_generated = 0
    def __init__(self, username: str = 'user', email: str = None, age: int = 18):
        self.username = username
        self.email = email
        self.age = age
        if email is None:
            self.email = f'{self.username}@example.com'
        TestDataFactory.total_generated += 1

    def __str__(self):
        return f"TestData(username='{self.username}', email='{self.email}', age={self.age})"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_default_user(cls):
        return cls(username="default_user", email="default@test.com", age=25)

    @classmethod
    def create_batch(cls, n: int) -> list:
        user_list = []
        i = 1
        for f in range(n):
            username = f'user_{i}'
            email = f'user_{i}@test.com'
            user = cls(username, email, 18)
            user_list.append(user)
            i += 1
        return user_list

print(TestDataFactory.total_generated)  # например, 0
batch = TestDataFactory.create_batch(3)
print(TestDataFactory.total_generated)  # должно стать 3
default = TestDataFactory.create_default_user()
print(TestDataFactory.total_generated)  # станет 4
print(TestDataFactory.create_batch(3))








