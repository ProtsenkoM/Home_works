"""3-
Створіть декоратор, який повертає результат функції. а також час за який вона виконана. Підсказка (для фіксації часу імпортуйте модуль time:  import time)"""

import time


def decorator(func):
    def wrapper(x):
        time_start_func = time.perf_counter()
        result = func(x)
        time_end_func = time.perf_counter()
        time_result = time_end_func - time_start_func
        print(f'Час виконання функції: {time_result:.9f} cекунд')
        return result
    return wrapper


@decorator
def square(a):
    return a ** 2


if __name__ == '__main__':
    print(square(100000))
    print(square(999))
    print(square(12345))
