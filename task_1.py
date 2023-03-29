# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии. 

def a_in_step(a, b):
    if b == 0:
        return 1
    return a * a_in_step(a, b - 1)

number_a = int(input('Введите число: '))
number_b = int(input('Введите степень: '))
print(a_in_step(number_a, number_b))
