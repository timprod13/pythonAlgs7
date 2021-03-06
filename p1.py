"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
    return array


def bubble_sort_w_smart_flag(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] < array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                flag = False
        if flag:
            break
    return array


def bubble_sort_from_lesson(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


input_array = [randint(-100, 100) for _ in range(100)]
array_w_sort = input_array.copy()
print(f"Original array:\n{input_array}")
print(f"Sorted array:\n{bubble_sort_w_smart_flag(array_w_sort)}")
# print(timeit(f"bubble_sort_from_lesson({numbers})",
#             setup="from __main__ import bubble_sort_from_lesson", number=10000))
time_orig = timeit(f"bubble_sort({input_array})", setup="from __main__ import bubble_sort", number=10000)
time_smart = timeit(f"bubble_sort_w_smart_flag({input_array})",
                    setup="from __main__ import bubble_sort_w_smart_flag", number=10000)
time_orig_sorted = timeit(f"bubble_sort({array_w_sort})", setup="from __main__ import bubble_sort", number=10000)
time_smart_sorted = timeit(f"bubble_sort_w_smart_flag({array_w_sort})",
                           setup="from __main__ import bubble_sort_w_smart_flag", number=10000)
print(f"Time complexity for original bubble sort: {time_orig}")
print(f"Time complexity for smart bubble sort:    {time_smart}")
print(f"Time complexity for original bubble sort with sorted array: {time_orig_sorted}")
print(f"Time complexity for smart bubble sort with sorted array:    {time_smart_sorted}")
'''Вывод:
Original array:
[-21, -4, 13, 26, -75, 93, -90, 17, 4, -25, -38, 62, -39, 83, 58, -75, 39, 77, -81, -71, 72, 91, 37, -6, -86, 42, -67,
-72, -72, -100, -74, 81, -42, -93, -36, 62, -9, 33, -88, 60, 5, -92, 55, -50, -42, 26, -15, 52, -83, -20, 45, 53, -11,
-8, 16, 100, -64, -11, -5, 15, -34, 86, 36, -98, 42, 41, -22, -64, 4, -96, 33, -23, 51, -18, 99, 27, 35, -3, -96, 76,
52, -80, 87, 5, -17, 42, 15, -97, 90, -34, 92, -82, -48, -60, 95, 100, 4, 83, -56, 2]
Sorted array:
[100, 100, 99, 95, 93, 92, 91, 90, 87, 86, 83, 83, 81, 77, 76, 72, 62, 62, 60, 58, 55, 53, 52, 52, 51, 45, 42, 42, 42,
41, 39, 37, 36, 35, 33, 33, 27, 26, 26, 17, 16, 15, 15, 13, 5, 5, 4, 4, 4, 2, -3, -4, -5, -6, -8, -9, -11, -11, -15,
-17, -18, -20, -21, -22, -23, -25, -34, -34, -36, -38, -39, -42, -42, -48, -50, -56, -60, -64, -64, -67, -71, -72,
-72, -74, -75, -75, -80, -81, -82, -83, -86, -88, -90, -92, -93, -96, -96, -97, -98, -100]
Time complexity for original bubble sort: 5.8411944
Time complexity for smart bubble sort:    5.9159117000000006
Time complexity for original bubble sort with sorted array: 3.292472400000001
Time complexity for smart bubble sort with sorted array:    0.0698445999999997
'''
# Для выполнения задачи использовал простейшее решение - флаг, который срабатывает в случае отсутствия сортировки за
# проход. Сортировку взял не из примера, а свою уже когда-то написанную функцию. Протестировал на timeit - 6.0110136,
# поэтому оставил свою. Оптимизирование функции дает прирост в скорости относительно неоптимизированной лишь в случае
# отсортированного массива, если же массив изначально не отсортирован - скорость работы функций практически
# идентична, т.е. иногда немного быстрее функция с оптимизацией, иногда - без неё. Поэтому "доработка" в случае
# неосортированного массива смысла не имеет
