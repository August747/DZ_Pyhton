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
has_upper = False
has_lower = False
has_spec = False
score=0

if len(password) >= 8:
     score += 1


for char in password:
    if char.isdigit():
        has_digit = True
        break
if has_digit:
    score += 1


for up in password:
    if up.isupper():
       has_upper = True
       break
if has_upper:
   score += 1


for lower in password:
    if lower.islower():
        has_lower = True
        break
if has_lower:
    score += 1


for spec in password:
    if not spec.isalnum():
        has_spec = True
        break
if not has_lower:
    score += 1

print ('Password score:', score)

if score < 5:
    print ('Recommendation:')
if len(password) < 8:
    print('The minimum password length is 8')
if has_digit == False:
    print('Use digits')
if has_upper == False:
    print('Use capital letters')
if has_lower == False:
    print('Use lower case letters')
if has_spec == False :
  print('Use special characters')