import math

x = float(input("Введіть x: "))

if x > 3:
    if x == 6:
        print("Помилка: логарифм від нуля не існує")
    else:
        f = 2.31 - math.log(abs(x - 6))
        print("f(x) =", f)

elif 0 <= x <= 3:
    f = math.cos(x + 3) + math.sin(2 * x + math.pi / 2)
    print("f(x) =", f)

else:
    f = 3 / x + math.exp(x) / (x ** 3)
    print("f(x) =", f)
