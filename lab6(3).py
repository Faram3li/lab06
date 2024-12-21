import math

def calculate_function(x):
    return x * math.sin(x) + math.exp(x)

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))

values = []
x = a
while x <= b:
    values.append(calculate_function(x))
    x += h

print("Значення функції (не відсортовані):")
print(", ".join(str(value) for value in values))

values.sort()

print("Значення функції (відсортовані):")
print(", ".join(str(value) for value in values))


