source="How are you?"
source.split() # ----> ['How','are','you?']

s= "one, two, three, four, five"
s.split() #     <----------- splits on space
s.split(", ") # <----------- splits on comma and space

def piglatinify_sentence(sentence):
  result_list= []
  for word in sentence.split():
    new_word = piglatin.piglatinify(word)
    result_list.append(new_item)
  result = ""
  # for item in result_list:
  #   result = result + item + " "
  # result = result.strip()
  # return result
  result = " ".join(result_list)
result = piglatinify_sentence(source)
padded_result = ":"+result+":"
print(source)
print(padded_result)