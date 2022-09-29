import piglatin     # < - - - since on same folder we can import

#Testing
test_word = "hello"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Able"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Able."
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "cable."
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Table!"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "deGromm"
result = piglatin(test_word)
print(test_word," -> ",result)