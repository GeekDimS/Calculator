operation = ''

def data_input(): # Функция для ввода данных
    a, b = input("Введите два числа через пробел").split()
    operation = input("Введите операцию")
    c, d = input("Введите два числа через пробел").split()
    first_number = [float(a), float(b)]
    second_number = [float(c), float(d)]
    return first_number, second_number, operation

def data_output(result): # Функция для вывода данных
    print(f'{result[0][0]} + i {result[0][1]} {operation}  {result[1][0]} +i{result[1][1]}')

def exit_or_not():
    lag = input("Если хотите продолжить - введите 1, если выйти - 0 и нажмите Enter")
    return(lag)  
