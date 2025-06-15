from typing import TypedDict

class UserInfo(TypedDict):
    name: str
    age: int

user = UserInfo(name="Ali", age=25)

# # print(type(user))         # <class 'dict'>
# # print(isinstance(user, dict))  # True
# # print(isinstance(user, object))  # True
# print(isinstance(user, UserInfo))  # TypeError: TypedDict does not support instance and class check
