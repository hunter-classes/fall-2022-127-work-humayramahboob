def initialize(name):
  """
  input a string in the form "First, Last
  return a string in the form "F. Last
  """
  # isolate, uppercase and add first init to result
  first = name[0]
  first = first.upper()
  result = result + first + "."
  
  # find the last name and capitalize it
  location = name.find(' ')
  last = name[location+1:].capitalize()

  return = result + ' ' + last
 


  