# Модуль, управляющий всей работой остальных модулей

import data_provider
# import main
import logger
import operations
import user_interface
def run():
    error = False
    #user_interface.Функция, отображающая запрос на ввод данных()
    input_data = data_provider.data_input() #Функция передачи чисел и операций, введённых пользователем
    #user_interface.Функция, отображающая введённую пользователем инфо(input_data)
    logger.operations_logger(error, f'{input_data[0][0]} + i{input_data[0][1]} {input_data[2]} {input_data[1][0]} + i{input_data[1][1]}', 'Ввод данных')#Функция, которая записывает в лог введённые пользователем данные(input_data)
    res_operation = operations.operation(input_data[0][0], input_data[0][1], input_data[1][0],input_data[1][1],input_data[2])
    logger.operations_logger(error, 'Результат вычислений : ', res_operation[2]) #Функция, которая записывает в лог результат вычислений(res_operation)
    data_provider.data_output(res_operation)#user_interface.Функция, отображающая реультат вычислений
    #  отображающая вопрос, закончить-ли работу калькулятора(res_operation)
    end = data_provider.exit_or_not() # Функция, возвращающая ответ, закончить-ли работу калькулятора()
    if end == 1:
        return False
    return True

