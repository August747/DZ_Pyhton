a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if b < a > c:
    max = a
if a < b > c:
    max = b
if a < c > b:
    max = c

print(max)
