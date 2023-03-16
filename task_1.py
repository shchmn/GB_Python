# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

number = int(input('Введите целое число: '))
zeroes = 0
ones = 0
for _ in range(number):
    coin = randint(0, 1)
    print(coin)
    if coin == 0:
        zeroes += 1
    else:
        ones += 1

if zeroes < ones:
    print(f'Необходимо перевернуть монеток: {zeroes}')
elif ones < zeroes:
    print(f'Необходимо перевернуть монеток: {ones}')
else:
    print('Равное количество монеток с гербом и решкой')