'''

Вывести треугольник #1 с шириной N с помощью цикла while
Вывести треугольник #2 с шириной N с помощью цикла while
'''
N = int(input('Enter the number: '))

while N > 0:
    print("*" * N)
    N -= 1

N = int(input('Enter the number: '))

b = 0
while N >= b:
    print("*" * b)
    b += 1

