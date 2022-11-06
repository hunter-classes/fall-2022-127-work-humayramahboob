# 1. Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

x = input("Please enter a sentence:")

x = x.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count_letters = {}
if char in alphabet:
  if char in count_letters:
    count_letters[char] = count_letters[char]+1
  else count_letters[char]=1

keys = count_letters.keys()
for char in sorted(keys):
  print(char,count_letter[char])

#Give the Python interpreter’s response to each of the following from a continuous interpreter session:

d = {'apples': 15, 'bananas': 35, 'grapes': 12} 
d['bananas'] #<-------- 35
d['oranges'] = 20
len(d) #<-------- returns 4 since there is 4 keys
'grapes' in d #<---------- returns True because dict has grapes
d['pears'] #<-------- gets nothing because there are no pears
d.get('pears', 0) #<------ gets 0 because there are no pears
fruits = d.keys() 
fruits.sort() #<------- sorted in {'grapes':12, 'apples':15, 'oranges':20, 'bananas':35}
print(fruits) 
del d['apples'] #<----- deletes key and value of apples
'apples' in d #<------ returns False because it will be gone
