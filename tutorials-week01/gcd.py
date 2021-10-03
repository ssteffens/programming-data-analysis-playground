# gcd = greatest common divisor
# program calculates greatest common divisor of two values (a and b)

a = 50
b = 20

while b > 0: 
    a, b = b, a % b

print(a)