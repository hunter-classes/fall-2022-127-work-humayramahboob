import csv

reader = csv.reader(open("school_scores.csv"))
max_test_takers = 0
state = ""
# I used the data from school scores to evaluate which state had the most amount of test takers.
for line in reader:
  if int(line[4]) > max_test_takers:
    max_test_takers = int(line[4])
    state = line[2]
print("The highest amount of SAT test takers are",max_test_takers,"from",state,".")

#------------------------------------------------------
#EXTRA 1: I compared the english and math averages to eachother for all states and compiled them into section on whoever has better math students, whoever has better english students, and whoever is equal.
skilled_in_math = []
skilled_in_english = []
equally_balanced = []
for line in reader:
  if int(line[9]) == int(line[12]):
    equally_balanced.append(line[2])
  elif int(line[9]) > int(line[12]):
    skilled_in_english.append(line[2])
  else:
    skilled_in_math.append(line[2])
balanced = ""
balanced = ", ".join(equally_balanced)
english = ""
english = ", ".join(skilled_in_english)
math = ""
math = ", ".join(skilled_in_math)
print("The states that have more skilled students in math are",math,"and the states that have more skilled students in english are", english, ". While the states that have equally balanced students are",balanced)

# ----------------------------------------------------- 
#EXTRA 2 I COMPARED THE HIGH ENGLISH AVERAGED STATES TO THE WHITE ONLY PERCENTAGES OF THOSE STATES FROM TWO DIFFERENT CSV FILES.
reader1 = csv.reader(open("state_demographics.csv"))
high_english_averages = []
for line in reader1:
  if int(line[9]) == 4:
    high_english_averages.append(line[2])

white_only_percentage = []
for line in reader:
  for word in line:
    if word in high_english_averages:
      white_only_percentage.append(line[8])
result = ""
result = ", ".join(high_english_averages)
result1= ""
result1= ", ".join(white_only_percentage)
print("The states",result,"have high english averages. The percentage of white only people in those states are",result1,". This concludes that states with the higher white only percentages have better english averages in school."
