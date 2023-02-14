"""Написать декоратор @cache который будет кэшировать входные и выходные данные функции. Для хранения входных и выходных
 данных нужно использовать словарь. Входные данные обязательно должны быть immutable типами. Важно что для каждой
 декорируемой функции должен быть свой словарь.



Пример:

Вызывается функция triangle_area с параметрами a=5, b=10

Мы проверяем в словаре что ранее эта функция вызывалась с такими параметрами, если нет, то вызываем функцию
triangle_area внутри декоратора и сохраняем в словарь параметры с которыми она вызывалась и результат который вернула и
возвращаем результат из декоратора.



Снова вызывается функция triangle_area с параметрами a=5, b=10

Мы проверяем в словаре что ранее эта функция вызывалась с такими параметрами, так как у нас ранее были сохранены входные
и выходные параметры функции, то мы можем не вызывать triangle_area внутри декоратора, и вернем прошлый результат
выполнения этой функции с параметрами a=5, b=10 из декоратора."""


def cache_decorator(func):
    data = {}

    def inner(*args):
        if data.get(tuple(args)) is None:
            value = func(*args)
            data[tuple(args)] = value
            return value
        else:
            return data[tuple(args)]
    return inner


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(x: float, y: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {x} и {y}')
    return (x * y) * 2


print('Результат выполнения triangle_area(5, 10):',
      triangle_area(5, 10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
print('Результат выполнения triangle_area(5, 10):',
      triangle_area(5, 10))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами
print('Результат выполнения circle_area(5, 10):',
      circle_area(5, 10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
print('Результат выполнения circle_area(5, 10):',
      circle_area(5, 10))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами
print('Результат выполнения triangle_area(5, 10):',
      triangle_area(5, 10))
