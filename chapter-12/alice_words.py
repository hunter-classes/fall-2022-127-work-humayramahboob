f = open('alice.txt','r')

alpha_list = {} 
for line in f:
  for word in line.split():
    word=word.replace('.','').replace(',','')
    word=word.replace('!','').replace('?','')
    word=word.replace('_','').replace('','')
    word=word.replace('(','').replace(')','')
    word=word.replace('[','').replace(']','')
    word=word.replace("'",'').replace(':','')
    word=word.replace(';','')

    word=word.lower()
    if word.isalpha():
      if word in alphab_list:
        alpha_list[word] alpha_list[word] + 1
      else:
        alpha_list[word]=1
keys = alpha_list.keys()
keys.sort()

saving = open('alice_words.txt','w')

for word in keys:
  saving.write(word + " " + str(count[word]))
  saving.write('\n')

print("The word alice appears",str(count('alice'),'times in the text.'))
