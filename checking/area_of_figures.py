from math import pi

figure = input()
area = 0
if figure == 'square':
    a = float(input())
    area = a ** 2
elif figure == 'rectangle':
     w = float(input())
     l = float(input())
     area = l * w
elif figure == 'circle':
     r = float(input())
     area = pi * r ** 2
elif figure == 'triangle':
     a = float(input())
     b = float(input())
     area = (a * b) / 2

print(f'{area: .3f}')







