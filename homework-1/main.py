def factorial(number: int) -> int:

    if number < 0: raise ValueError

    result = 1

    for element in range(1, number+1):
        result *= element

    """
    Лучший случай - Константная сложность
    Средний - Линейная сложность
    Худший - Факториальная сложность
    """

    return result



def fibonacci(number: int) -> list:

    if number < 0: raise ValueError

    result = [0, 1]
    if number == 0: result = [0]

    for element in range(number):
        fib_number = result[-1] + result[-2]
        result.append(fib_number)

    if number != 0: result.remove(result[-1])

    """
    Лучший случай - Константная сложность
    Средний - Линейная сложность
    Худший - Линейная сложность
    """

    return result



def count_ones(number: int) -> int:

    if number < 0: raise ValueError
    if not number.is_integer(): raise TypeError

    result = 0

    while number:
        remind = number % 2
        number //= 2

        if remind == 1:
            result += 1

    """
    Лучший случай - Константная сложность
    Средний - Линейная сложность
    Худший - Линейная сложность
    """

    return result


def palindrome(number: int) -> bool:

    if number < 0: return False
    if not number.is_integer(): raise TypeError

    result = False
    new_numbers = []
    true_count = 0

    while number:
        new_numbers.append(number % 10)
        number //= 10

    need_true_count = len(new_numbers) // 2

    for i in range(len(new_numbers)):
        if len(new_numbers) != 0 and new_numbers[0] == new_numbers[-1] and len(new_numbers) != 1:
            true_count += 1

            new_numbers.pop(0)

            if len(new_numbers) != 0:
                new_numbers.pop(-1)

    if need_true_count == true_count:
        result = True

    return result



def gcd(number1: int, number2: int) -> int:

    if number1 < 0: raise ValueError
    if number2 < 0: raise ValueError
    if not number1.is_integer(): raise TypeError
    if not number2.is_integer(): raise TypeError

    result = [min(number1, number2), max(number1, number2)]
    result1 = [result[0], result[1]]

    while result1[0] != result1[1] and result1[1] != 0:

        result1[0], result1[1] = min(result), max(result)
        result = result1

        result[1] = result[1] % result[0]

    return result1[0]