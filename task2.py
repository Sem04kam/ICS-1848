import sys
import math

x = float(sys.argv[1])
y = float(sys.argv[2])

AB = math.sqrt(x ** 2 + y ** 2)
BC = AB
AC = 2 * abs(x)

print("AB =", AB)
print("BC =", BC)
print("AC =", AC)