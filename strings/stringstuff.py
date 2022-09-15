s1 = "Hello World"
s2 = 'another string'

s3 = """
This is a multiline string
we use the triplle quotes
for this
"""

s4 = s1+s1

print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))

print(s1.upper) # THIS MAKES A NEW STRING

# isolate the world from s1
# first find the space
space_location = s1.find(" ")
print(space_loction)
# pull out from 6 (one after thr space until the end)
s5 = s1[space_location+1:] # nothing after the : means go to the end
print(s5)
print(s5)