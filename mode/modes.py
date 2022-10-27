# 1. findLargest(l) which takes in a list of numbers and returns the value of the largest number
def findLargest(l):
  max = l[0]
  for i in l:
    if i> max:
      i = max
  return max
    
# freq(l,v) which takes a list of numbers(l) and a value (v). The function will return the frequency of v, that is, the number of times v appears in l.
def freq(l,v):
  total = 0
  for i in l:
    if i == v:
      total = total+1
  return total
