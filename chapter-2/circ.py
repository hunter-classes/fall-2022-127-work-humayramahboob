#8 Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

import math 
r=input("Enter the radius of the circle:")
float_r = float(r)
area = math.pi*(float_r**2)
print('When the radius of the circle is',r,', the area of the circle is',area)