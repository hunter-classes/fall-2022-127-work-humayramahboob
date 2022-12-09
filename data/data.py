for line in school_scores:
  if float(line[4]) > max_test_takers:
    max_test_takers = float(line[4])
    state = line[2]
print("The highest amount of SAT test takers are",max_test_takers,"from",state,".")

#------------------------------------------------------
#EXTRA 1: I compared the english and math averages to eachother for all states and compiled them into section on whoever has better math students, whoever has better english students, and whoever is equal.
skilled_in_math = []
skilled_in_english = []
equally_balanced = []
for line in school_scores:
  if float(line[9]) == float(line[12]):
    equally_balanced.append(line[2])
  elif float(line[9]) > float(line[12]):
    skilled_in_english.append(line[2])
  else:
    skilled_in_math.append(line[2])
balanced = ""
balanced = ", ".join(equally_balanced)
english = ""
english = ", ".join(skilled_in_english)
math = ""
math = ", ".join(skilled_in_math)
print("The states that have more skilled students in math:",math)
print("------------------------------------------------------------")
print("The states that have more skilled students in english:",english)
print("------------------------------------------------------------")
print("The states that have equally balanced students are:",balanced)
print("------------------------------------------------------------")

# ----------------------------------------------------- 
#EXTRA 2 I COMPARED THE HIGH ENGLISH AVERAGED STATES TO THE WHITE ONLY PERCENTAGES OF THOSE STATES FROM TWO DIFFERENT CSV FILES.
prompt = csv.reader(open("state_demographics.csv"))
state_demographics = []
for item in prompt:
  state_demographics.append(item)
del state_demographics[0]
max_white_only = 0
for item in state_demographics:
  if float(item[8]) > float(max_white_only):
    max_white_only = item[8]
    state = item[0]
print("In",state,"there are the most white only people with a percentage of",max_white_only)