"""1-
Створіть декоратор, який виводить в консоль назву викликаної функції. 
Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення. 
Під час виклику цих функцій має бути повернутий результат операції, а ім’я викликаної функції має відображатися на консолі разом із результатом.
Маленька підказка (__name__)"""


def decorator(func):
    def wrapper(*args):
        print(f"Назва функції: {func.__name__}")
        result = func(*args)
        return result
    return wrapper

@decorator
def summarize(a, b):
    return a+b

@decorator
def multiplication(a, b):
    return a*b


if __name__ == '__main__':
    print(summarize(4,5))
    print(multiplication(5,6))
    print(summarize(9,5))
    print(multiplication(6,6))

