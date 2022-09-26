# Add a new program named fizzbuzz.py. When run, it should count from 1 to 100. If the number is
# divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5,
# print "fizzbuzz"

i = 0
while i<100:
    i = i+1
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%3==0 and i%5==0:
        print("fizzbuzz")
    else:
        print(i)