n = int(input("Введіть кількість рядків: "))

words = []

for i in range(n):
    text = input("Введіть рядок: ")
    words += text.split()

longest = max(words, key=len)

for i in range(len(words)):
    if words[i] == longest:
        words[i] = longest[::-1]
        break

print("Результат:", " ".join(words))
