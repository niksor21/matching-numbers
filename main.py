a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if (a == b == c) == True:
    print('3 числа одинаковые')
elif (a == b) | (b == c) | (c == a) == True:
    print('2 числа одинаковые')
else:
    print('Нет одинаковых чисел')