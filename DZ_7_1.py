'''
Задание 1:

Запросить у пользователя 5 чисел и записать их в список



Задание 2:

Дан список A = [1, 2, 3, 4, 5]

Удалить последнее число из списка



Задание 3:

Запросить у пользователя 10 чисел и записать их в список A

Запросить у пользователя число N

Вывести пользователю сколько в списке A повторяется число N



Задание 4:

Запросить у пользователя число N

Запросить у пользователя N чисел и записать их в список A

Вывести список в обратной последовательности



Задание 5:

Запросить у пользователя 5 чисел и записать их в список A

Записать все числа из списка A которые больше 5 в список C



Задание 6:

Запросить у пользователя число N

Запросить у пользователя N целых чисел и записать их в список A

Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.



Задание 7:

Пользователь вводит текст нужно вывести количество цифр в этом тексте

Пример:

> 'Lorem 222 ipsum, 123 dolor 1 sit amet

Количество цифр: 7
'''
a = input('Enter firs number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
d = input('Enter fourth number: ')
e = input('Enter fifth number: ')

s = [a, b, c, d, e]
print(s)



A = [1, 2, 3, 4, 5]
A.pop(4)
print(A)



num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')
num3 = input('Enter 3rd number: ')
num4 = input('Enter 4th number: ')
num5 = input('Enter 5th number: ')
num6 = input('Enter 6th number: ')
num7 = input('Enter 7th number: ')
num8 = input('Enter 8th number: ')
num9 = input('Enter 9tn number: ')
num10 = input('Enter 10ер number: ')

A = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

N = input('Enter your search number: ')

for N in A:
    print(N.count(A))


