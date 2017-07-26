'''Function that takes as a parameters number1(int), number2(int) and number3 and return the count of integers
that are divisible by number3 in range [number1, number2]'''


def handle_numbers(number1, number2, number3):

    result = 0

    for i in range(number1, number2 + 1):
        if i % number3 == 0:
            result += 1

    return result

