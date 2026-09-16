import math

def func(x):
    value = abs(2 * x + 7)
    if value == 0:
        return None

    root = math.copysign(abs(x - 4) ** (1 / 3), x - 4)
    return math.log(value, 5) + root


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

n = int((b - a) / h)

for i in range(n + 1):
    x = a + i * h
    result = func(x)

    if result is None:
        print("x =", x, "f(x) не існує")
    else:
        print("x =", round(x, 3), "f(x) =", round(result, 5))
