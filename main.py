Random Art Generatorimport turtle
import random
c = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
c.bgcolor(50, 30, 50)
for i in range(100):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  t.goto(x,y)
  sideLength = i*2
  for x in range(random.randint(5,20)):
    t.forward(sideLength)	
    t.left(123)
  t.penup