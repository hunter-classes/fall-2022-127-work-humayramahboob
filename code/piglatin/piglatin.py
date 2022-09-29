def bondify(name):
  # find the first name and capitalize it
  location = name.find(' ')
  first = name[:location].capitalize()
  
  # find the last name and capitalize it
  last = name[location+1:].capitalize()
  # write the string that returns
  return last + ' ' + first +' ' + last


def piglatin(word):
  # keep track of punctuations
  if word[-1] in ".!?":
    end_of_sent = True
    punctuation = word[-1]
    word = word[:-1]
  else:
    end_of_sent = False
  # keep track of if the word had a capital letter
  if first == first.upper():
    capital = True
  else:
    capital = False
  
  word = word[0].lower()+word[1:]
  first = word[0]
  
  if first in 'aeiou':
    result = word + 'yay'
  else:
    result = word[1:]+first+'ay'
  # if we started with a capital letter we
  # have to transform the result back to have
  # a capital letter
  if capital:
    result = result.capitalize()
# return the punctuation to the end if it had one
  if end_of_sent:
    result = result + punctuation 
  return result

