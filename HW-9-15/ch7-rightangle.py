# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as

def isRightAngle(a,b,c):
# c is the longest
  sum = a*a + b*b
  return abs(math.sqrt(sum)-c) < 0.001
  
def isRightAngle2(a, b, c):           
  #making sure other sides can be longer
    return isRightAngle(a,b,c) or \
            isRightAngle(b,c,a) or \
             isRightAngle(a,c,b)

print isRightAngle2()