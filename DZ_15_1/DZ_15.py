"""адание 1

Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

Задание 2

Запросить у пользователя текст и записать его в файл data.txt

Задание 3

Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

Задание 4

Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

Задание 5

Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

Задание 6

Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

Задание 7

Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:

'в' - 20 раз

'привет' - 10 раз

'как' - 9 раз

'у' - 7

'world' - 4"""
import random
from collections import Counter

# numbers = []
# text = (open('file.txt', 'r'))
# txt1 = text.read()
# new_text = txt1.replace('.', '').split()
#
# for i in new_text:
#     if i.isdigit():
#         numbers.append(i)
# print(numbers)


# text = input('Enter your text: ')
# file = open('data.txt', 'w')
# file.write(text)


# nums = ''
# N = int(input('Enter your N number: '))
# for i in range(1, N + 1):
#     num = input(f'Enter your {i} number: ')
#     nums = f'{nums} {num}'
# print(nums)
# file = open('numbers.txt', 'w')
# file.write(str(nums))


# file = open('random_numbers.txt', 'w')
# random_numbers = []
# for i in range(100):
#     a = random.randint(1, 100)
#     random_numbers.append(a)
# for i in random_numbers:
#     x = (f'{i}\n')
#     file.write(str(x))


# text = open('random_text.txt', 'r')
# text = text.read()
# words = len(text.split())
# print(words)


# nums = open('numbers.txt', 'r')
# nums = nums.read()
# summa = 0
# for i in nums:
#     if i.isdigit():
#         summa += int(i)
# print(summa)


text = open('random_text.txt', 'r')
text = text.read()
a = text.split()
# b = Counter(a)
print(a)
