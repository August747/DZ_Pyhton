N = int(input('Enter number N: '))
if N > 0:
    a = input(f'Enter {N} numbers: ')
    b = [a]
    b = a.split()
    print(sorted(b, reverse=True))
else:
    print('Wrong number')

