import math

# Example values
a = 3
b = 4
c = 5
height = 4  # height corresponding to base b

# Area using base and height
area_base_height = 0.5 * b * height

# Perimeter
perimeter = a + b + c

# Heron's formula
s = (a + b + c) / 2
area_heron = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Pythagorean theorem check (right triangle)
is_right_triangle = c**2 == a**2 + b**2

# Output
print(f"Area (base × height): {area_base_height}")
print(f"Area (Heron's formula): {area_heron}")
print(f"Perimeter: {perimeter}")
print(f"Is Right Triangle: {is_right_triangle}")

