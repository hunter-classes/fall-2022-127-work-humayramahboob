import turtle

def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  #draw a hexagon
  for i in range(6):
    t.forward(sidelen)
    t.left(60)

def ngon(t,numsides,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  #draw a ngon
  for i in range(numsides):
    t.forward(sidelen)
    t.left(360/numsides)

wn = turtle.Screen()
crush = turtle.Turtle()

hexagon(crush,10,10,3,"blue",50)
ngon(crush,8,100,100,3,"pink",50)

wn.exitonclick()