import operator

OPERATORS = {'*': operator.mul, '/': operator.truediv,
             '+': operator.add, '-': operator.sub}

REAL_TYPE = "real"
COMPLEX_TYPE = "complex"


def calculation_operation(number1, number2, math_opetrator):
        return OPERATORS[math_opetrator](number1, number2)

def check_number_type(b):
    if b == 0: return REAL_TYPE
    else:
        return COMPLEX_TYPE

def operation(a1, b1, a2, b2, op):
    number1_type = check_number_type(b1)
    number2_type = check_number_type(b2)

    error = False
    error_or_result_text =""
    result = 0
    number1 = complex(a1, b1) if number1_type == COMPLEX_TYPE else a1
    number2 = complex(a2, b2) if number2_type == COMPLEX_TYPE else a2

    result = calculation_operation(number1, number2, op)
    if result.imag == 0:
        result = result.real
    # print(result.imag == 0, result.real)
    error_or_result_text = f'{number1} {op} {number2} = '
    return (error, error_or_result_text, result)


# print(operation(6, -2, -3, 4, '+'))