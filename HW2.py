s = 'swim'
r = 'run'

a = 2
b = 500
c = 8
d = -52

f = 0.5
g = -0.84
h = 0.33333334

print(a > b)
print(a < b)
print(b >= d)
print(c <= d)
print(a != b)
print(a > b and c <= d)
print(a < d or b >= d)
print(not (a > b))
print(a < d and not c <= d)
print(a > b or a < d or c > d)
print(a > b and c > b and c > d)
print(a > b and (c > b or c < d))
print(b < a and (c < b or c < d))
print(not (a > b or d < c))
print(a != b or c >= d)

print(f > g)
print(g >= h)
print(not f > g)
print(f == g or h == f)
print(g < f <= h)
print(not (g < h or f > h))
print(g != h)
print(f == h)
print(f > h != g)

print(s > r)
print(r > s)
print(r == s)
print(not s > r)
print(s != r)
print(r >= s)
print(not r != s)
print(s == "swim")
print(s == "run")
print(r <= s)

num = int(input("Введите число: "))
if num > 30:
    rez = "больше"
elif num < 30:
    rez = "меньше"
else:
    rez = "равно"
print("Вы ввели число =", num, ",которое", rez, "30")


import random

num = int(input("Введите число: "))
rndm = (random.randint(1, 100))
if num > rndm:
    print("Вы ввели число =", num, ",которое больше сгенерированного числа:", rndm)
elif num < rndm:
    print("Вы ввели число =", num, ",которое меньше сгенерированного числа:", rndm)
else:
    print("Вы ввели число =", num, ',которое равно сгенерированному числу:', rndm)


num = int(input("Введите число: "))
rndm1 = (random.randint(1, 100))
rndm2 = (random.randint(1, 100))
if num > rndm1:
    rez1 = "больше"
elif num < rndm1:
    rez1 = "меньше"
else:
    rez1 = "равно"
if num > rndm2:
    rez2 = "больше"
elif num < rndm2:
    rez2 = "меньше"
else:
    rez2 = "равно"
print("Вы ввели число =", num, ",которое", rez1, "первого сгенерированного числа:", rndm1, "и", rez2, "второго сгенерированного числа:", rndm2)