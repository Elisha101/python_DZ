# Задача 16: Требуется вычислить, сколько раз встречается некоторое число
# X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# N = int(input('Введите размер элемента: '))
# list_1 = map(int, (input('Введите элементы списка, через пробел: ').split()))
# x = int(input('Введите кол-во х: '))
# count = 0
# for i in list_1:
#     if i == x:
#         count += 1
# print(f'Число {x} встречается в списке: {count} раз')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

# N = int(input('Введите кол-во элемента массива А: '))
# a = [int(input('Введите целое число: ')) for i in range(N)]
# x = int(input('Введите заданное число х: '))
# b = [abs(a[i]-x) for i in range(len(a))]
# print(a[b.index(min(b))])


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n1 = int(input('Введите количество элементов первого набора чисел: '))
n2 = int(input('Введите количество элементов второго набора чисел: '))
arr1 = []
arr2 = []
for i in range(n1):
    arr1.append(int(input('Введите элемент первого массива: ')))
for j in range(n2):
    arr2.append(int(input('Введите элемент второго массива: ')))
arr3 = []
for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)
arr3.sort()
print(arr3)


'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''

import random
kust = int(input("Введите количество кустов: "))
berryes = list(random.randint(0, 10) for i in range(kust))
result = []
i = 0
sum = 0

print(berryes)

while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"максимальное число ягод за одну итерацию {result[-1]}")