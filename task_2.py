# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

from random import randint

n = int(input('Введите натуральное число: '))
x = int(input('Введите искомое число: '))
mass = []
min_raz = 50
near_min = 0
for _ in range(n):
    mass.append(randint(1, 50))

for i in mass:
    if i - x < min_raz and i - x >= 0:
        min_raz = i - x
        near_min = i

print(mass)
print(f'ближайшее число = {near_min}')
