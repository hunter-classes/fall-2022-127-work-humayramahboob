# 1. findLargest(l) which takes in a list of numbers and returns the value of the largest number
def findLargest(dataset):
  max = dataset[0]
  for i in dataset[1:]:
    if i> max:
      i = max
  return max
    
# freq(l,v) which takes a list of numbers(l) and a value (v). The function will return the frequency of v, that is, the number of times v appears in l.
def freq(dataset,v):
  total = 0
  for i in dataset:
    if i == v:
      total = total+1
  return total

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

def=testMode(size,maxValue):
  dataset = buildRandomList(size,maxValue)
  print(dataset)
  t = datetime.datetime.now()
  starttime = t.microsecond / 1000
  m = mode(dataset)
  end = datetime.datetime.now()
  elapsed = (end.microsecond / 1000)-starttime
  print("size:",size,"time:",elapsed)
    