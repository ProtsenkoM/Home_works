"""2-
Створіть функцію, яка може повертати квадрати парних чисел у діапазоні від 0 до 1000000000 включно. Рішення має працювати і не фрізити комп’ютер."""


def firstn(range_of_numbers):
    for num in range(range_of_numbers + 1):
        if num % 2 == 0:
            yield num ** 2


if __name__ == '__main__':
    result = firstn(1000000000)
    for i in result:
        print(i)
