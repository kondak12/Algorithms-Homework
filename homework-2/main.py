def max_in_range(array: list[int or float], start: int, end: int):

    if not start.is_integer(): raise TypeError
    if not end.is_integer(): raise TypeError

    """
    Функция для поиска максимального числа в поставленных границах списка

    :param array: Список чисел
    :param start: Начальный индекс
    :param end: Конечный индекс
    :return: Максимальное число в диапазоне; Обсалютный и Относительный индексы этого числа;

    Случаи сложности:
        Худший - Линейная
        Средний - Линейная
        Лучший - Линейная
    """

    new_array = array[start:end:]
    result = array[start]
    coord_index = 0

    for i in range(len(new_array)):

        if new_array[i] > result:

            result = new_array[i]
            coord_index = i

    abs_index = coord_index + start

    return result, abs_index, coord_index



#############################################



def binary_search(array: list[int or float], target: int or float) -> int: # вопрос

    """
    Функция для бинарного поиска в списке(незаконченная)

    :param array: Список для бинарного поиска
    :param target: Искомый элемент
    :return: Индекс найденного или не найденного(-1) элемента

    Случаи сложности:
        Худший - Логарифмическая
        Средний - Логарифмическая
        Лучший - Линейная
    """

    result = -1
    middle_index = len(array) // 2

    if target in array:

        array.sort()

        if array[middle_index] == target:
            result = middle_index

        elif target > array[middle_index]:
            result = binary_search(array[middle_index:len(array) + 1:1], target)

        elif target < array[middle_index]:
            result = binary_search(array[0:middle_index:1], target)

    return result



def bubble_sort(array: list[int or float]) -> list[int or float]:

    """
    Функция сортировки методом 'Пузырька'

    :param array: Список для сортировки
    :return: Отсортированный список

    Случаи сложности:
        Худший - Квадратичная
        Средний - Квадратичная
        Лучший - Константная ?
    """

    for i in range(len(array)):

        if i != len(array) - 1 and array[i] > array[i + 1]:

            number = array[i]
            array[i] = array[i + 1]
            array[i + 1] = number

            bubble_sort(array)

    return array



def three_sum(array: list[int]) -> list[list[int]]:

    """
    Функция для нахождения всех уникальных троек элементов, сумма которых равна 0

    :param array: Список чисел
    :return: Массив с тройками, которые в сумме образуют 0

    Случаи сложности:
        Худший - Квадратичная
        Средний - Квадратичная
        Лучший - Константная ?
    """

    result = []

    for i in range(len(array)):

        for j in range(i + 1, len(array)):

            for ii in range(j + 1, len(array)):

                if array[i] + array[j] + array[ii] == 0:
                    result.append([array[i], array[j], array[ii]])

    return result