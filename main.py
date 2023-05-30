# Задача №1

# Функция ввода и проверки на целое число
def input_number(name):
    while True:
        x = input('Введите целое число %s:\n' % name)
        try:
            x = int(x)
            return x
            break
        except ValueError:
            print('Это не целое число')

# Функция ввода одной из двух операций и выполнения требуемого действия
def input_operation_2(a,b,c):
    while True:
        x = input('Введите операцию + или *:\n')
        if x == '+':
            return a + b + c
            break
        elif x == '*':
            return a * b * c
            break
        else:
            print('Вы ввели неверную операцию')

a = input_number('a')
b = input_number('b')
c = input_number('c')
print('Результат:', input_operation_2(a,b,c))



# Задача №2

# Функция ввода одного из четырёх операторов с проверкой ввода
def input_operation_4():
    while True:
        x = input('Введите операцию +, -, * или /:\n')
        if x in ['+', '-', '*', '/']:
            return x
            break
        else:
            print('Вы ввели неверную операцию')

# Функция калькулятора с использованием выбранного оператора
def calculator(oper):
    a = input_number('a')
    b = input_number('b')
    match oper:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b

oper = input_operation_4()
print('Результат:', calculator(oper))