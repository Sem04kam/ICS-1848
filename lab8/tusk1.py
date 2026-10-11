import random

A = [random.randint(3, 15) for i in range(8)]

even = 0
odd = 0

for x in A:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

B = [even, odd, sum(A)]

print("Масив A:", A)
print("Масив B:", B)
