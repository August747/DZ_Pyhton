"""Необходимо создать класс Human с атрибутами:

name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:

get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info"""
class Human:

    def __init__(self, name: str, surname: str, age: int, phone: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        print(f'{self.name}, {self.surname}, {self.age}, {self.phone}, {self.address}')

    def call(self, phone_number: int):
        print (f" {self.phone} вызывает абонента {phone_number}")



vlad = Human('Vlad', 'Ostapenko', 25, 380501231231, 'Kharkov')
vlad.get_info()
vlad.call(380991234141)
nastya = Human('Nastya', 'Ivanova', 21, 380661231231, 'Kiev')
nastya.get_info()
misha = Human('Misha', 'Gremlin', 35, 380971231231,  'Tatarbynari')
misha.get_info()

