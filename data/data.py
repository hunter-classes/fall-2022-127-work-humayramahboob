import csv

reader = csv.reader(open("school_scores.csv"))
school_scores = []
for line in reader:
  school_scores.append(line)
del school_scores[0]

max_test_takers = 0
state = ""
# I used the data from school scores to evaluate which state had the most amount of test takers.
for line in school_scores:
  if int(line[4]) > max_test_takers:
    max_test_takers = int(line[4])
    state = line[2]
print("The highest amount of SAT test takers are",max_test_takers,"from",state,".")

#------------------------------------------------------
#EXTRA 1: I compared the english and math averages to eachother for all states and compiled them into section on whoever has better math students, whoever has better english students, and whoever is equal.
skilled_in_math = []
skilled_in_english = []
equally_balanced = []
for line in school_scores:
  if float(line[9]) == float(line[13]):
    equally_balanced.append(line[2])
  elif float(line[9]) > float(line[13]):
    skilled_in_english.append(line[2])
  else:
    skilled_in_math.append(line[2])
balanced = ""
balanced = ", ".join(equally_balanced)
english = ""
english = ", ".join(skilled_in_english)
math = ""
math = ", ".join(skilled_in_math)
print("The areas that have more skilled students in math:",math)
print("------------------------------------------------------------")
print("The areas that have more skilled students in english:",english)
print("------------------------------------------------------------")
print("The areas that have equally balanced students are:",balanced)
print("------------------------------------------------------------")

# ----------------------------------------------------- 
#EXTRA 2 I Compared the english and math averages of people with the highest white only percentage and lower white only percentge to see if they make a difference in averages.
prompt = csv.reader(open("state_demographics.csv"))
state_demographics = []
for item in prompt:
  state_demographics.append(item)
del state_demographics[0]

max_white_only = 0
index = 0
for item in state_demographics:
  if float(item[8]) > float(max_white_only):
    max_white_only = item[8]
    state = item[0]
    for line in school_scores:
      if line[2] == state:
        math_grade = line[13]
        english_grade = line[9]

min_white_only = item[8]
for item in state_demographics:
  if float(item[8]) < float(min_white_only):
    min_white_only = item[8]
    state1 = item[0] 
    for line in school_scores:
      if line[2] == state1:
        math_grade1 = line[13]
        english_grade1 = line[9]
print("In",state,"there are the most white only people with a percentage of",max_white_only,". Students have a english average of",english_grade,"and a math average of",math_grade,". In",state1,"there are the least white only people with a percentage of",min_white_only,". Students have a english avaerage of",english_grade1,"and a math average of",math_grade1,".")