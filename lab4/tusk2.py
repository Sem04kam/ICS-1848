import math

def func(x, y):
    value = abs(math.sin(math.pi / 4 + 2.31 * x))

    if value == 0:
        return None

    W = (
        (math.sin(x) - math.cos(y))
        * 4.138
        * math.log(value)
    )

    return W


x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

result = func(x, y)

if result is None:
    print("Вираз не визначений")
else:
    print("W =", result)
