"""Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python. 
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.
"""
TEST_DICT = {
    "Java": "James Gosling",
    "Python": "Guido van Rossum",
    "C++": "Bjarne Stroustrup",
    "Basic":"John Kemeny"
}
for key, value in TEST_DICT.items():
    print(f'My favorite programming language is: {key}.  It was created by {value}.')

del TEST_DICT["Basic"]

print (TEST_DICT)