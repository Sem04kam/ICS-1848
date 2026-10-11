import random

a = int(input("Введіть a: "))
a = abs(a)

M = []

for i in range(3):
    row = []
    for j in range(4):
        row.append(random.randint(-a, a))
    M.append(row)

print("Початковий масив:")
for row in M:
    print(row)

maximum = max(max(row) for row in M)

for i in range(3):
    for j in range(4):
        if M[i][j] == 0:
            M[i][j] = maximum

A = M[0]
B = M[1]
C = M[2]

print("Змінений масив:")
for row in M:
    print(row)

print("Максимальний елемент:", maximum)
print("Масив A:", A)
print("Масив B:", B)
print("Масив C:", C)
