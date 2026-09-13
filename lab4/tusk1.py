import math

x = float(input("Введіть x: "))

if x < 0:
    print("Помилка: x повинен бути >= 0")
else:
    f = (
        (math.exp(0.9 * x + 4) + math.pow(x + 2 * x**2, 1 / 4))
        / (6 * math.log(abs(x + 2) + 1))
        - 9 * math.cos(0.7 * x + math.sqrt(x))
    )

    print("f(x) =", f)
