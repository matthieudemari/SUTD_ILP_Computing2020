"""
Author: Matthieu DE MARI

Description: computes and prints the determinant and the roots,
of a given quadratic equation ax^2 + bx + c = 0,
with strictly positive determinant.

Inputs: Requires the user to specify values of the parameters
a, b, and c. These should be numbers, ideally floats.

Outputs: this script calculates and prints the values of the
determinant and both roots.

Important note: if the determinant is not strictly positive,
then the roots will be incorrect.
"""

# ----------------------------------------
# 1. Define the coefficients (a,b,c) of
# the quadratic equation

a = 2
b = -2
c = -24

# ----------------------------------------
# 2. Compute the discriminant delta

delta = b**2 - 4*a*c 

# ----------------------------------------
# 3.Print delta to check it is strictly positive

print(delta)

# ----------------------------------------
# 4. Compute the two roots (x1, x2)

x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)

# ----------------------------------------
# 5. Print the roots

print(x1)
print(x2)