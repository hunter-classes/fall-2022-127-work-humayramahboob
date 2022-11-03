import datetime
import random

# 1. findLargest(l) which takes in a list of numbers and returns the value of the largest number
def findLargest(dataset):
  max = dataset[0]
  for i in dataset[1:]:
    if i> max:
      i = max
  return max
    
# freq(l,v) which takes a list of numbers(l) and a value (v). The function will return the frequency of v, that is, the number of times v appears in l.
def freq(dataset,v):
#  total = 0
#  for i in dataset:
#    if i == v:
#      total = total+1
#  return total
  return len([x for x in dataset x == v])

def buildRandomList(size,maxvalue):
  result = [random.randrange(maxvalue) for x in range(size)]
  return result

def mode(dataset):
  """
  Returns a mode of the dataset, that is the value that appears most frequently
  
  If multiple values appear the same # of times and are most frquent, return any of them.
  
Ex: mode([5,4,5,6,7,8,5,4)] -->5 since 5 appears the  most
mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since both of those values appear 3 times which is the most
"""
  modeSoFar = dataset[0]
  freqSoFar = freq(dataset,mode)
  for item in dataset[1:]:
    if freq(dataset,item) > freqSofar:
      modeSoFar = item
      freqSoFar = freq(dataset,item)
  return modeSoFar

def fastMode(dataset):
  largest = findLargest(dataset)
  tallies = [0 for x in range(largest+1)]
  for item in dataset:
    tallies[item] = tallies[item] + 1
  mode_count = findLargest(tallies)
  for i in range(len(tallies)):
    if tallies[i] == mode_count:
      return i
  return i
  return tallies
  
def testMode(size,maxValue):
  print("Dataset Size:",size)
  dataset = buildRandomList(size,maxValue)
  # print(dataset)
  m = mode(dataset)
  print("Mode:",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

def testFastMode(size,maxValue):
  print("Dataset Size: ",size)
  dataset = buildRandomList(size,maxValue)
  m = fastMode(dataset)
  print("Fast Mode: ",m)

for item in dataset:
  x = x do something with dataset
  z = x + y
  if z > something:
    something
  else:
    something else
    
x = 5 
y = 10
if x > y:
  z = x + y
else:
  z = x * y
  z = z*z
z = x+y
z = z*z
print(z)
