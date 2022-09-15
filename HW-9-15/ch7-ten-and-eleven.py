#10 and 11
# Write a function is_rightangled which, given the length of three sides of a triangle, 
# will determine whether the triangle is right-angled. Assume that the third argument to the 
# function is always the longest side. It will return True if the triangle is right-angled, or 
# False otherwise.

# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test 
# floating point numbers for equality. If a good programmer wants to know whether x is equal or
# close enough to y, they would probably code it up as

from test import testEqual

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled