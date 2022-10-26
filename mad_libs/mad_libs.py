import random
#EXTRA #1: I will make a function that opens a file and seperates the words on it line by line. def file_translator(f) 
def file_translator(f):
  new_f=open(f)
  data = new_f.read()
  lines =data.split('\n')
  words =data.split()
  return words

def mad_libs_filler(MAIN,NOUN,VERB,prompt):
  prompt_list=[]
  # EXTRA #2: (MAKING SURE THE MAIN CHARACTER STAYS THE SAME) To make sure you pick a main randomly and the same main is used throughout the madlibs solution, we need to use the random.choice() function outside the for function so it only picks randomly once.
  main= random.choice(MAIN)
  for item in prompt:
# We use .append(main) since we have a set person from the list to use all the time. For verbs and nouns, you pick random from the list multiple times.
    if item == "<MAIN>":
      prompt_list.append(main.capitalize())
    elif item == "<VERB>":
      prompt_list.append(random.choice(VERB))
    elif item == "<NOUN>":
      prompt_list.append(random.choice(NOUN))
    else:
      prompt_list.append(item)
  result = ""
  result = " ".join(prompt_list)
# EXTRA #3: To make sure that the first word stays capitalized after replacing it, I divide the lines up and then capitalized the first letter. I don't use the capitalize command since it gets rid of the capitals throughout the sentence.
  lines = result.split('. ')
  capitalized = []
  for line in lines:
    first = line[0]
    new_result = first.upper() + line[1:]
    capitalized.append(new_result)
  result = ""
  result = ". ".join(capitalized)
  return result

NOUN = ["car","house","tree","whale","store","hose","jar","pickle"]
VERB =["eat","sleep","dance","vape","jump","run","walk","trip"]
MAIN = ["john","juan","mary","susan","bill","klee","tammy","drake"]

#TESTING FIRST MAD LIBS STORY
prompt = file_translator('one.dat')
print(mad_libs_filler(MAIN,NOUN,VERB,prompt))

print("----------------------------------------------------")
#TESTING SECOND MAD LIBS STORY
prompt = file_translator('two.dat')
print(mad_libs_filler(MAIN,NOUN,VERB,prompt))