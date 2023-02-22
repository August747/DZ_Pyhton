"""Создайте супер класс Shape и его наследников Triangle, Rectangle.
Класс Shape содержит абстрактный метод draw
Класс Triangle в инициализаторе принимает параметр width: int - ширина треугольника и реализует метод draw (Выводит в
консоль треугольник с шириной width)
Класс Rectangle в инициализаторе принимает параметр width: int и height: int - ширина, высота прямоугольника и реализует
метод draw (Выводит в консоль прямоугольник с шириной width и высотой height)
Создайте список с этими фигурами и в цикле вызовите метод draw у этих обьектов


P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним) главное чтобы состоял и был заполнен
символом '*'.
Прямоугольник тоже должен состоять и быть заполнен символом '*'.
Важно: Используйте аннотации!"""
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self):
        for i in range(self.width):
            a = i * '*'
            print(f'{a}')


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.height):
            y = self.width * '*'
            print(y)


triangle = Triangle(7)
rectangle = Rectangle(8, 8)
shapes = [triangle, rectangle]
for i in shapes:
    i.draw()