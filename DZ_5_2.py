'''

Задание со звездочкой:

Вывести треугольник #3 с шириной N с помощью цикла while
Вывести треугольник #4 с шириной N с помощью цикла while

'''
N = int(input('Enter the number: '))

b=0

while N > 0 :
    print((b * " ") + ('*' * N))
    b += 1
    N -= 1

N = int(input('Enter the number: '))

b=0

while N >= 0:
    if N == 0:
        break
    b += 1
    N -= 1
    print((N * " ") + ('*' * b))




