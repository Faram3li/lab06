import math

def calculate_function(x):
    return x * math.sin(x) + math.exp(x)
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))

x_values = []
f_values = []
x = a
while x <= b:
    f_value = calculate_function(x)
    x_values.append(x)
    f_values.append(f_value)
    x += h

print("Значення функції:")
for x, f in zip(x_values, f_values):
    print(f"x = {x:.2f}, f(x) = {f:.2f}")
