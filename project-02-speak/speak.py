# EXTRA #1 READING FILE AND PUTTING INTO DICTIONARY   
f = open('pirate.dat')
data = f.read()
pirate_dict = dict(s.split(':') for s in data.split('\n'))

#this reads the text and splits into words
t =open('input.txt')
input = t.read()
input = input.lower()
words = input.split()

# this function converts into pirate language
def pirate_speak(words):
  new_input = []
  for item in words:
    if item in pirate_dict.keys():
      new_input.append(pirate_dict[item])
    else:
      new_input.append(item)
  result = ""
  result = " ".join(new_input)
  # EXTRA #2 to deal with capitals, I divide the lines and capitalize the first letter.
  lines = result.split('. ')
  capitalized = []
  for line in lines:
    first = line[0]
    new_result = first.upper() + line[1:]
    capitalized.append(new_result)
  result = ""
  result = ". ".join(capitalized)
  return result

print("The original input:"," ".join(words))
print("------------------------------------------")
print("The input in pirate language:",pirate_speak(words))
