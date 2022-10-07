# Write a function to find the smallest value in a listKfind smallest in a list of items
def listKfind(lst):
  min = list[0]
  for i in lst:
    if i < min:
      min = i
  return min
  
# Write a function that returns a new list that contains all the odd items in the original list
def odd_numbers(lst):
  odd_list = []
  for i in lst:
    if i%2!=0:
      odd_list.append(i)
  return odd_list

# Write a function that takes a string and returns a new string where all the words are capitalized.
def capitalized(s):
  words = s.split(" ")
  s1 = ""
  for word in words:
    new_word = word.capitalize()
    s1 = s1 + " " + new_word
  return s1

# Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
def uppercase_long(s):
  words = s.split(" ")
  new_s = ""
  for word in words:
    if len(word) > 5:
      new_word = word.upper()
      new_s = new_s + " " + new_word
    return new_s

# Write a function that takes a list of numbers and returns a new list with each item squared
def squared(lst):
  squared_list= []
  for i in lst:
    squared_list.append(i*i)
  return squared_list

# Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
def corresponding_sum(lst1,lst2):
  total = []
  index = 0
  for i in lst1:
    total.append(lst1[index]+lst2[index])
    index = index + 1
  return total

# chapter 10 # 10, 11, 12
# 10. Count how many words in a list have length 5.
def length_five(lst):
  total = 0
  for word in lst:
      if len(word) == 5:
          total = total + 1
  return total

# 11.Sum all the elements in a list up to but not including the first even number.
def sum(lst):
  sum = 0
  index = 0
  while index < len(lst) and lst[index] % 2 != 0:
      sum = sum + lst[index]
      index = index + 1
  return sum

# Count how many words occur in a list up to and including the first occurrence of the word “sam”.
def not_sam(lst):
  sum = 0
  index = 0
  while index < len(lst) and lst[index] != "sam":
      sum = sum + 1
      index = index + 1
  if lst[index]== "sam":
      sum = sum + 1
  return sum