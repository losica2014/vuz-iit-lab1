from math import sqrt

a,b,c = list(map(int, [input() for _ in range(3)]))

d = b**2 - 4*a*c
if(d < 0): print('Нет корней')
elif(d == 0):
    x = (-b)/(2*a)

    print(x)
else:
    drt = sqrt(d)
    x1 = (-b+drt)/(2*a)
    x2 = (-b-drt)/(2*a)

    print(x1, x2)