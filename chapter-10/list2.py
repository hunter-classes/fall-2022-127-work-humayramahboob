# 4. Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
def average(numsList):
  total = 0
  for num in numsList:
    total = total + num
  return total / len(numsList)

# 6. Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
def sum_of_squares(xs):
  sum = 0
  for num in xs:
    sum = sum + num*num
  return sum

grades = [90,95,100,90]
print("grades:",grades)
average = average(grades)
print("Average:",average)

l = [3,4,5]
print("l:",l)
print("sum of squares:",sum_of_squares(l))