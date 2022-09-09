import turtle

def sample_function():
  print("This is a function")
  print("It can be used multiple times")

def square(t,x,y,w,color,sidelen):
  """
  Parameters:
  t = turtle
  x,y = location
  w = width
  color = color to draw in
  sidelen = lenght of sides
  """
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  # draw a square
  for i in range(4):
    t.forward(sidelen)
    t.right(90)

def triangle(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  #draw a triangle
  for i in range(3):
    t.forward(sidelen)
    t.left(120)


wn = turtle.Screen()
crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,-30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)

triangle(crush,200,200,3,"pink",50)

wn.exitonclick()
wn.mainloop()
