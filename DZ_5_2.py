'''

Вывести треугольник #3 с шириной N с помощью цикла while

'''
N = int(input('Enter the number: '))

a = ' '
while N > 0 :
    print(a, "*" * N)
    N -= 1

