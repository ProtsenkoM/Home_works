"""
4 - написати власну функцію map, використовуючи callback
    
"""

def custom_map(callback, iterable):
    result = []
    for i in iterable:
        x = callback(i)
        result.append(x)
    return result

def square(x):
    result = x ** 2
    return result


if __name__ == '__main__':
    print(custom_map(square, [1, 2, 3, 4, 5, 6]))
    print(custom_map(square, [1,4,6,7,9]))
