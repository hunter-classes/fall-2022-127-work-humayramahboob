# Write a function called is_even(n) that takes an integer as an argument and returns 
# True if the argument is an even number and False if it is odd.

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def is_even_short_version(n):
  return n%2 == 0

# Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
    if n%2==0:
        return False
    else:
        return True

def is_odd_short_version(n):
  return not(is_even(n))

print("Even tests")
result = is_even(10)
print("Result for 10 is:",result)
result = is_even(11)
print("Result for 11 is:",result)

print("Direct call:",is_even(11))

print("Odd tests")
result = is_odd(10)
print("Result for 10 is:",result)
result = is_odd(11)
print("Result for 11 is:",result)

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

# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
  return "Hello " + name + "!"

# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word
# is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  return out[:2] + word + out[2:]

# Given a string, return the string made of its first two chars, so the String 
# "Hello" yields "He". If the string is shorter than length 2, return whatever there 
# is, so "X" yields "X", and the empty string "" yields the empty string "".


def first_two(str):
  return str[:2]