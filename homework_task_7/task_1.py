
"""1 -
Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно. 
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями."""


def sum_range(start, end):
    if start > end:
        start, end = end, start
    x = sum(range(start, end + 1))
    return x


if __name__ == '__main__':
    print(sum_range(1, 5))
    print(sum_range(4, 1))
