number = int(input("Введіть чотирицифрове число: "))

if 1000 <= number <= 9999:
    a = number // 1000
    b = (number // 100) % 10
    c = (number // 10) % 10
    d = number % 10

    minimum = min(a, b, c, d)
    maximum = max(a, b, c, d)

    result = minimum * maximum

    print("Найменша цифра:", minimum)
    print("Найбільша цифра:", maximum)
    print("Добуток:", result)

else:
    print("Помилка: потрібно ввести чотирицифрове число")
