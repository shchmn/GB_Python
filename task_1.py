# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
a = number // 100
b = number // 10 % 10
c = number % 10
print(f'Сумма цифр числа {number} равна {a + b + c}')