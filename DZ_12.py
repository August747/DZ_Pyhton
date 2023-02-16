"""
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:

запись – W;

чтение – R;

запуск – X.

На вход программе подается:

число n – количество файлов;

n строк с именами файлов и допустимыми операциями;

число m – количество запросов к файлам;

m запросов вида «операция файл».

Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt
"""
n = int(input('Enter the number of files: '))
access_rights = {'R': 'read',
                 'X': 'execute',
                 'W': 'write'}
files = {}
answer = []
x = 'OK'
y = 'Access denied'

for i in range(n):
    a = input('Enter your file: ').split()
    files[a[0]] = [access_rights[i] for i in a[1:]]
m = int(input('Enter the number of file requests: '))
for i in range(m):
    premissions, b = input('Enter validation and file: ').split()
    if premissions in files[b]:
        answer.append(x)
    else:
        answer.append(y)
for i in range(len(answer)):
    print(answer[i])
