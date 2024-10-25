# making original function for plus
def original_plus(number1, number2):
    result = number1 + number2
    return result

def plus_plus(number1):
    number1 += number1
    # same as
    # number1 = number1 + number1
    return number1

def minus_minus(number1):
    number2 = 100
    number2 -= number1
    # number2 = number2 - number1
    return number2

result = original_plus(1,2)
print(result) #=> 3

result = original_plus(100, 300)
print(result) #=> 400

result = plus_plus(5)
print(result)

result = minus_minus(5)
print(result)