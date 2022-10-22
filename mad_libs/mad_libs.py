import random
#EXTRA #1: I will make a function that opens a file and seperates the words on it line by line. def file_translator(f) 
def file_translator(f):
  new_f=open(f)
  data = new_f.read()
  lines =data.split()
  return lines
  f_list=[]
  for item in lines:
    f_list.append(lines.split(" "))
  return f_list


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
  return result

NOUN = ["tree","material","water","lion","tiger","bear","food"]
VERB =["eat","watch","play","run","attack","hit","share","make"]
MAIN = ["sam","chase","sara","hunter","bailey","ash","shaniqua"]

#TESTING FIRST MAD LIBS STORY
prompt = file_translator('one.dat')
print(mad_libs_filler(MAIN,NOUN,VERB,prompt))

#TESTING SECOND MAD LIBS STORY