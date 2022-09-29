# Add a new program named fizzbuzz.py. When run, it should count from 1 to 100. If the number is
# divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5,
# print "fizzbuzz"

def fizzbuzz(n):
  i = 1
  while i< n: # can also use for number in range(1,n):
  i = i+1
  if i%3==0 and i%5==0:
    print("fizzbuzz")
  elif i%3==0:
    print("fizz")
  elif i%5==0:
    print("buzz")
  else:
    print(i)

value = 20
print("Fizzbuss up to ".value)
fizzbuzz(value)