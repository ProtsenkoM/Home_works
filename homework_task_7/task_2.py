"""2 -
Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення : периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх"""

def square (side):
    perimeter = 4 * side
    square =  side ** 2
    diagonal = (side * (2 ** 0.5))
    return {
        'Perimeter': perimeter, 
        'Square':square,
        'Diagonal': diagonal
    }




if __name__== '__main__':
    result = square(10)
    print(f"Периметр квадрата = {result['Perimeter']}, площа квадрату = {result['Square']}, діагональ квадрату = {result['Diagonal']:.2f} ")

    result = square(5)
    print(f"Периметр квадрата = {result['Perimeter']}, площа квадрату = {result['Square']}, діагональ квадрату = {result['Diagonal']:.2f} ")