"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
import timeit


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left_part = array[:mid]
    right_part = array[mid:]
    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)
    result = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    result += left_part[i:]
    result += right_part[j:]
    return result


def merge_sort_2(array):
    n = len(array)
    if n < 2:
        return array
    l = merge_sort(array[:n // 2])
    r = merge_sort(array[n // 2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r) or l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    return res


def merge_sort_from_lesson(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_from_lesson(left)
        merge_sort_from_lesson(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


list_size = int(input("Введите число элементов: "))
input_list = [random.random() * 50 for _ in range(list_size)]
list_w_sort = input_list.copy()
print(f"Исходный -                 {input_list}")
print(f"Отсортированный -          {merge_sort(list_w_sort)}")
list_w_sort = input_list.copy()
print(f"Отсортированный_2 -        {merge_sort_2(list_w_sort)}")
list_w_sort = input_list.copy()
print(f"Отсортированный из урока - {merge_sort_from_lesson(list_w_sort)}")
print(timeit.timeit("merge_sort(input_list[:])",
                    setup="from __main__ import merge_sort, input_list", number=10000))
print(timeit.timeit("merge_sort_from_lesson(input_list[:])",
                    setup="from __main__ import merge_sort_from_lesson, input_list", number=10000))
print(timeit.timeit("merge_sort_2(input_list[:])",
                    setup="from __main__ import merge_sort_2, input_list", number=10000))
"""Вывод:
Введите число элементов: 10
Исходный -                 [15.802359926553095, 29.251813163018266, 47.53363994675247, 32.9474558067242,
 30.76113302314858, 26.01782008817315, 37.051302109143414, 12.16924897915868, 43.98463254529256, 44.02740671337156]
Отсортированный -          [12.16924897915868, 15.802359926553095, 26.01782008817315, 29.251813163018266,
 30.76113302314858, 32.9474558067242, 37.051302109143414, 43.98463254529256, 44.02740671337156, 47.53363994675247]
Отсортированный из урока - [12.16924897915868, 15.802359926553095, 26.01782008817315, 29.251813163018266,
 30.76113302314858, 32.9474558067242, 37.051302109143414, 43.98463254529256, 44.02740671337156, 47.53363994675247]
0.12354639999999995
0.12496090000000026
"""
# Нашёл чуть более упрощенный по реализации вариант, но, как оказалось, время отработки у них практически идентично,
# поэтому нашёл ещё один вариант, однако время его отработки оказалось самым большим
"""Итоговый вывод:
Введите число элементов: 10
Исходный -                 [18.236824715618795, 37.836379842526085, 15.726591082907488, 45.517945765711424, 
21.05929896506572, 16.25180555138809, 39.57568437891292, 44.87022999388294, 19.13963688355692, 7.960039312333722]
Отсортированный -          [7.960039312333722, 15.726591082907488, 16.25180555138809, 18.236824715618795, 
19.13963688355692, 21.05929896506572, 37.836379842526085, 39.57568437891292, 44.87022999388294, 45.517945765711424]
Отсортированный_2 -        [7.960039312333722, 15.726591082907488, 16.25180555138809, 18.236824715618795, 
19.13963688355692, 21.05929896506572, 37.836379842526085, 39.57568437891292, 44.87022999388294, 45.517945765711424]
Отсортированный из урока - [7.960039312333722, 15.726591082907488, 16.25180555138809, 18.236824715618795, 
19.13963688355692, 21.05929896506572, 37.836379842526085, 39.57568437891292, 44.87022999388294, 45.517945765711424]
0.1282124
0.12742279999999995
0.1308784999999999
"""
