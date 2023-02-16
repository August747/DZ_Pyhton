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

A = [ for i in range(6)]
# A = [number = int(input(f'Enter your {i} number: ')) for i in range(5) A.append(number)]
print(A)



A = [1, 2, 3, 4, 5]
A.pop(4)
print(A)



A = []
score = 0
for i in range(1,11,1):
    number = int(input(f'Enter your {i} number: '))
    A.append(number)

N = int(input('Enter your search number: '))

print('Your number of search number equals:', A.count(N))



N = int(input('Enter number N: '))
A = []
N += 1
for N in range(1,N,1):
    number = int(input(f'Enter your {N} number: '))
    A.append(number)
A.reverse()
print(A)



A = []
C = []
for i in range(1,6):
    number = int(input(f'Enter your {i} number: '))
    A.append(number)
    if number > 5:
        C.append(number)
print(A)
print(C)



N = int(input('Enter your ''N'' number: '))
A = []
for i in range(N):
    number = int(input(f'Enter {i + 1} integer number: '))
    A.append(number)
    if i == 0:
      max_number = number
      min_number = number
      continue
    elif number > max_number:
        max_number = number
        continue
    elif number < min_number:
        min_number = number
print('Your minimum number: ', min_number)
print('Your maximum number: ', max_number)



text = []
a = input('Введите ваш текст: ')
text.append(a)
score = 0

for char in a:
    if char.isdigit():
        score += 1

print(text)
print('Количество цифр: ', score)