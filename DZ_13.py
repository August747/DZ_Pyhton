"""
1)Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. В исходном списке минимум 2 элемента.
2)Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
3)Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
"""
def change(lst):
    if len(lst) < 2:
        return ('Enter list with 2 numbers at least')
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst



def to_dict(lst):
    dict_list = {}
    for i in range(len(lst)):
        dict_list[lst[i]] = lst[i]
    return dict_list



def sum_range(start, end) -> int:
    sum = 0
    if start > end:
        for i in range(end, start + 1, 1):
            sum += i
        return sum
    for i in range(start, end + 1, 1):
        sum += i
    return sum