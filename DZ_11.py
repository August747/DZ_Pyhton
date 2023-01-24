"""
Дано два множества A и B

В множестве А находятся имена должников за Сентябрь

В множестве B находятся имена должников за Октябрь

Найти:

* Вывести имена людей которые должны за Сентябрь и Октябрь

* Вывести должников за Октябрь у которых нет долга за Сентябрь


"""

A = {'Мария', 'Александр', 'Петр', 'Рома', 'Игорь', 'Василий', 'Григорий'}
B = {'Мария', 'Александр', 'Петр', 'Рома', 'Степан', 'Семен', 'Виталий'}

C = A | B
print(C)
D = B - A
print(D)
