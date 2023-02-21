"""Дан список словарей, необходимо записать их в файл с помощью модуля pickle. В каждом из словарей одинаковый набор
ключей, а все значения представлены в виде строк.

Дано два словаря
A = {'key': 1}
B = {'key1: 2}
Необходимо написать код который будет их объединять
Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы не потерять значения
нужно записать в один ключ список в котором будут находится значения.

Записать результат в файл result.json в формате JSON."""
import pickle
import json

# dict_list = [{'sky': 'blue', 'grass': 'green'},
#              {'sky': 'red', 'grass': 'yellow'},
#              {'sky': 'black', 'grass': 'dark blue'}]
#
# with open('data.bin', 'wb') as f:
#     data = pickle.dumps(dict_list)
#     f.write(data)
#
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}



def dict_update(x: dict, y: dict) -> dict:
    for key, value in y.items():
        if key in x:
            a = []
            a.append(x[key])
            a.append(value)
            x[key] = a
        else:
            x[key] = value
    C = x
    return C


C = dict_update(A, B)
with open('result.json', 'w') as f:
    f.write(json.dumps(C))
