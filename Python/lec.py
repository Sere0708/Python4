# 1. Вычислить число c заданной точностью d

# Пример:

# - при d = 3, π = 3.141


# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)


# N = int (input ('Введите число: '))

# for d in range (1, N // 2 + 1) :
#   if N % d == 0 :
    # print (d, ' ', sep = '', end = '')
# print (N)




# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")




