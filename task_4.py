# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 

n = int(input('Введите количество долек шоколадки по вертикали: '))
m = int(input('Введите количество долек шоколадки по горизонтали: '))
k = int(input('Введите количество долек, которые нужно отломить: '))

if k == n or k == m:
    print('Можно')
elif k < min(n, m) or k == n * m or k > max(n, m):
    print('Нельзя')
elif k % n == 0 or k % m == 0:
    print('Можно')
else:
    print('Нельзя')