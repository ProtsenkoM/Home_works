"""3 -
Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
Ця функція намалює простий прямокутник заданої висоти та ширини, використовуючи character для друку ліній. Наприклад, display_box(5, 4, 'x') має вивести наступне:
xxxxx
x x
x x
xxxxx"""


def display_box(width: int, height: int, character="*"):
    if width <=0 or height <=0:
        print("Невірні розміри прямокутника")

    for i in range(height):
        if i == 0 or i == height - 1:
            print (width * character)
        else:
            print(character + ' ' * (width - 2) + character)


if __name__=='__main__':
   display_box(5, 4, 'x') 
   display_box(15, 8, 'x')
   display_box(25, 15, 'x')
   display_box(0, 15, 'x')