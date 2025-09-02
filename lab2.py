name = 'Ivan'
age = 19
height = 5.4
favorite_color = 'Black'

print(name)
print(age)
print(height)
print(favorite_color)

print(f"Hello, my name is {name} and I am {age} years old!")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}
""")

from math import pi
circle_area = pi*(5**2)
print(f'{circle_area:.1f}')

import math
from math import sqrt, sin, cos
sqrt_age = sqrt(age)
sin_height = sin(height)
cos_height = cos(height)
print(f'{sqrt_age:.2f}', f'{sin_height:.2f}', f'{cos_height:.2f}')

sum = age+5
difference = height-4
product = age*height
quotient = height/2
remainder = age//3
power = age**2
print(sum, f'{difference:.1f}', f'{product:.1f}', quotient, remainder, power)


Fahrenheit = float(input('Enter Fahrenheit: '))
Celsius = (Fahrenheit - 32) * 5/9
print('Celsius:', f'{Celsius:.1f}')










