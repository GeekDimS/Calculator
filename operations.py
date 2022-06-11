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
    result = 0

    if number1_type == number2_type == COMPLEX_TYPE:
        number1 = complex(a1, b1)
        number2 = complex(a2, b2)
        print(number1, number2)
        result = calculation_operation(number1, number2, op)
        # print(number1, number2, result)
    elif  number1_type == number2_type == REAL_TYPE:
        number1 = a1
        number2 = a2
        result = calculation_operation(number1, number2, op)
        # print(number1, number2, result)
    else:
        error = True


    return (error, result)


# print(operation(6, 4, -3, -2, '*'))