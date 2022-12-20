'''

Программа запрашивает у пользователя пароль и записывает в переменную password.

Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5

Проверки:

Длина пароля больше или равно 8 символам
В пароле есть хотя бы одна цифра
В пароле есть хотя бы одна большая
В пароле есть хотя бы одна маленькая буква
В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же рекомендации по улучшению пароля.

'''

password = input('Enter your password: ')

has_digit = False
has_Upper = False
has_lower = False
score=0

if len(password) >= 8:
    score += 1
else:
    print ('Recommendation: The minimum password length is 8')


for char in password:
    if char.isdigit():
        has_digit = True
        break
if has_digit:
    score += 1
else:
    print ('Recommendation: Use digits ')

for up in password:
    if up.isupper():
        has_Upper = True
        break
if has_Upper:
    score += 1
else:
    print ('Recommendation: Use capital letters')


for lower in password:
    if lower.islower():
        has_lower = True
        break
if has_lower:
    score += 1
else:
    print ('Recommendation: Use lower case letters')



print (score)