import math
import random


def f(x):
    arg_log = abs(2 * x + 7)
    if arg_log == 0:
        return None
    log_part = math.log(arg_log) / math.log(5)
    arg_root = x - 4
    root_part = math.copysign(abs(arg_root) ** (1 / 3), arg_root)
    return log_part + root_part


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

values = []
x = a
while x <= b + 1e-9:
    y = f(x)
    if y is not None:
        values.append(round(y, 4))
    x += h

print("Список у рядок:")
print(*values)

if len(values) > 1:
    min_idx = values.index(min(values))
    max_idx = values.index(max(values))

    start_idx = min(min_idx, max_idx)
    end_idx = max(min_idx, max_idx)

    if end_idx - start_idx > 1:
        sub_list = values[start_idx + 1 : end_idx]
        print("\nЕлементи між найменшим і найбільшим:")
        print(sub_list)

        random.shuffle(sub_list)
        print("Перемішаний список (рандом):")
        print(sub_list)
    else:
        print("\nМіж мінімумом та максимумом немає елементів.")
