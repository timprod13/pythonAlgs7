"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from statistics import median
import numpy
import timeit
from random import random


def solve_by_median(my_list):
    return median(my_list)


# Было интересно насколько быстро отработает numpy
def solve_by_numpy(my_list):
    return int(numpy.median(my_list))


# Функция хоть и не использует сортировку и написана простым кодом, имеет шанс ошибиться примерно в половине случаев
# из-за того, что в ней мы находим медиану списка через среднее арифметическое, коим в списке медиана может и не быть.
# В любом случае я пытался, надеюсь, что идеальный вариант хоть немного похож на написанный мной
def solve_by_average(my_list):
    total_sum = 0
    diff_array = []
    for num in my_list:
        total_sum = total_sum + num
        diff_array.append(num)
    average = total_sum / len(my_list)
    # print(average)
    for i in range(len(diff_array)):
        diff_array[i] = abs(average - diff_array[i])
    # print(diff_array)
    for i in range(100):
        for j in range(len(diff_array)):
            if diff_array[j] < i:
                # здесь ещё нужно дописать, что делать при равных результатах при вычислении разности, но ситуации
                # это не изменит
                return my_list[j]


# Поэтому для сортировки возьмем алгоритм Шелла:
def solve_by_shell(my_list):
    my_list_m = my_list.copy()
    halves = len(my_list_m) // 2
    while halves:
        for i, el in enumerate(my_list_m):
            while i >= halves and my_list_m[i - halves] > el:
                my_list_m[i] = my_list_m[i - halves]
                i -= halves
            my_list_m[i] = el
        halves = 1 if halves == 2 \
            else int(halves * 5.0 / 11)
    len_central = len(my_list) // 2
    for i in range(len_central):
        my_list_m.pop()
    return my_list_m.pop()


m = int(random() * 100)
len_arr = 2 * m + 1
input_list = list(map(int, [random() * 50 for _ in range(len_arr)]))
print(f"m is {m}\nArray length is {len_arr}\nOriginal array: {input_list}")
print("Answer with median is          ", solve_by_median(input_list), "and it's time complexity is",
      timeit.timeit("median(input_list[:])", setup="from __main__ import median, input_list", number=1))
print("Answer with numpy is           ", solve_by_numpy(input_list), "and it's time complexity is",
      timeit.timeit("solve_by_numpy(input_list[:])", setup="from __main__ import solve_by_numpy, input_list", number=1))
print("Answer with unsorted method is ", solve_by_average(input_list), "and it's time complexity is",
      timeit.timeit("solve_by_average(input_list[:])", setup="from __main__ import solve_by_average, input_list", number=1))
print("Answer with Shell method is    ", solve_by_shell(input_list), "and it's time complexity is",
      timeit.timeit("solve_by_shell(input_list[:])", setup="from __main__ import solve_by_shell, input_list", number=1))
""" Вывод с большим количеством элемнтов:
m is 87
Array length is 175
Original array: [0, 20, 3, 0, 30, 45, 26, 9, 29, 10, 10, 35, 37, 17, 35, 9, 39, 35, 0, 41, 15, 22, 24, 19, 27, 15, 14, 
4, 37, 45, 35, 15, 12, 38, 22, 37, 8, 29, 27, 44, 20, 15, 24, 44, 13, 5, 37, 0, 2, 41, 12, 22, 42, 2, 40, 17, 18, 48, 
33, 36, 43, 18, 3, 45, 15, 2, 44, 19, 36, 30, 38, 35, 16, 22, 4, 6, 31, 33, 28, 44, 39, 29, 5, 6, 3, 28, 11, 47, 36, 3, 
35, 14, 20, 48, 35, 47, 16, 35, 18, 12, 37, 1, 38, 27, 46, 21, 21, 32, 21, 29, 25, 3, 46, 29, 41, 0, 20, 47, 46, 9, 14, 
24, 15, 14, 26, 26, 13, 39, 9, 15, 15, 37, 1, 19, 48, 27, 34, 19, 42, 2, 37, 25, 25, 8, 48, 36, 36, 15, 29, 31, 7, 28, 
2, 23, 44, 3, 2, 26, 10, 18, 4, 31, 29, 36, 47, 40, 3, 21, 25, 18, 9, 12, 31, 28, 18]
Answer with median is           24 and it's time complexity is 1.6100000000018877e-05
Answer with numpy is            24 and it's time complexity is 7.229999999999737e-05
Answer with unsorted method is  24 and it's time complexity is 4.7400000000002995e-05
Answer with Shell method is     24 and it's time complexity is 0.00018119999999999248
"""

""" И с малым:
m is 1
Array length is 3
Original array: [10, 10, 48]
Answer with median is           10 and it's time complexity is 2.6000000000192536e-06
Answer with numpy is            10 and it's time complexity is 5.4200000000004245e-05
Answer with unsorted method is  10 and it's time complexity is 1.2099999999987121e-05
Answer with Shell method is     10 and it's time complexity is 5.900000000003125e-06
"""

# Итак, проведение тестов показало, что numpy отстаёт от остальных трёх, третье место занимает ненадежное среднее
# арифметическое, метод Шелла по скорости же отстаёт от стандартной median, причем это заметнее на тестах с большим
# количеством элементов в списке
