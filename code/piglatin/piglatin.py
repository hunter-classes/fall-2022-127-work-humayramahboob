def bondify(name):
  # find the first name and capitalize it
  location = name.find(' ')
  first = name[:location].capitalize()
  
  # find the last name and capitalize it
  last = name[location+1:].capitalize()
  # write the string that returns
  return last + ' ' + first +' ' + last

# Task: deal with punctuations
def piglatin(word):
  first = word[0]
  if first in 'aeiou':
    result = word + 'yay'
    final = result.capitalize()
  else: 
    result = word[1:] + first + 'ay'
    final = result.capitalize()
  return final


#TESTS
test_word = "james bond"
result = bondify(test_word)
print ("Bondify:",test_word, "->", result)
test_word = "hello"
result = piglatin(test_word)
print("Piglatin:",test_word, "->", result)
test_word = "able"
result = piglatin(test_word)
print("Piglatin:",test_word, "->", result)