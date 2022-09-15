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