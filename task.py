from math import log10, tan , sin


fruit = 'pear'
print(fruit)

score = 100
if score >= 60:
    print('Good mark!')
else:
    print('Bad mark!')

is_even = False
is_odd = True
print(not is_even)
print(not is_odd)
print(is_even and is_odd)
print(is_even or is_odd)

x = 4.123
y= 2.395
result = log10(x**3) + tan(y) + (y + x)**3 - (x * sin(y + 1.6)) / (177 * x**2)
print(result)
