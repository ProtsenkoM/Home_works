"""
2 ¬- У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] , перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]
"""


camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snace_case_list = []

for camel_case_var in camel_case_list:
    snake_case_var = ''.join(['_'+ var.lower() if var.isupper() else var for var in camel_case_var])
    if snake_case_var.startswith('_'):
        snace_case_list.append(snake_case_var[1:])
print(snace_case_list)