text = input("Введіть рядок: ")

upper = ""
lower = ""

for i in text:
    if i.isupper():
        upper += i
    elif i.islower():
        lower += i

print("Великі літери:", upper)
print("Малі літери:", lower)
print("Кількість великих літер:", len(upper))
print("Кількість малих літер:", len(lower))
