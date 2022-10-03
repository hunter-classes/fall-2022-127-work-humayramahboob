# 5. Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
def max(nums):
  max = 0
  for i in nums:
    if i>max:
      max = i
  return i 

# 7. Write a function to count how many odd numbers are in a list.
def odd(lst):
  amount = 0
  for num in lst:
    if num%2!=0:
      amount = amount + 1
  return amount

# 8. Sum up all the even numbers in a list.
def sum_of_even_numbers(lst):
  sum = 0
  for num in lst:
    if num%2=0:
      sum = sum + num
  return sum
    