"""
2-
Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
* Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
* Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
* Якщо введені числа не можуть бути float спіймайте ValueError
* Також ловіть помилку при діленні на 0
* В кожній спійманій помилці друкуйте пояснення, що пішло не так
* За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором, якщо введені не вірні дані
* Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
* Результат виконання формули - float число з двома знаками після крапки
""" 

class FormulaError(Exception):
    pass
class WrongOperatorError(Exception):
    pass
error_count = 3
while error_count!= 0:
    try:
        str_input = input("Введіть вираз (наприклад, 2 * 5): ")
        list_elem = (str_input.split())
        if len(list_elem)!=3:
            raise FormulaError('Невірна формула')
        if list_elem[1] not in ('*', '/', '+','-'):
            raise WrongOperatorError('Не вірний оператор')
        try:
            num_1 = float(list_elem[0])
            num_2 = float(list_elem[2])
        except (ValueError) as e:
            raise ValueError('Недійсні числа')    
        print(f'Результат дорівнює: {(eval(str_input)):.2f}') 
    except ZeroDivisionError:
        print ('Помилка: Ділити на нуль не можна') 
        error_count -= 1
    except (FormulaError,WrongOperatorError,ValueError) as e:
        print(f"Помилка: {e}")
        error_count -= 1
    else: 
        print('Помилок немає')
    finally:
        another_calc = input("Бажаєте продовжити? (Так/Ні): ")
        if another_calc.lower() != 'так':
            print(f'Программу завершено.')
            break
        elif error_count == 0:
            print('Кількість не вірних спроб = 3, программу було завершено.')
            break
            
