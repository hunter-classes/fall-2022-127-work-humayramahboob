def bondify(name):
  """
  input a string in the form "First Last
  return a string in the form "Last First Last
  """
  
  # find the first name
  location = name.find(' ')
  first = name[:location].capitalize()
  
  # find the last name
  last = name[location+1:].capitalize()
  # write the string that returns
  return last + ' ' + first +' ' + last


def piglatin(word):
  """
  input: a string representing a word 
  returns: a new string with the word converted 
  to piglatin
 
  Rules:
  if the first letter is a consonent, move it 
  from the start to the end and add "ay" so 
 "hello" becomes "ellohay"

 If the first letter is a vowel, just add "yay" 
 to the end

 try to also handle upper case word
 """
  
  if word.startswith('a' or 'e' or 'i' or 'o' or 'u'):
    result = word + 'yay'
    return result
  else:
    result = word[1:] + word[0] + 'ay'
    return result