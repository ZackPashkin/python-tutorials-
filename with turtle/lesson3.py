import turtle

# initialize the turtle and the app interface
turtle.shape('turtle')

# adjust the turtle size
turtle.shapesize(2)

# adjust the color
turtle.color('red','blue')

# adjust the speed
turtle.speed(20)

def draw_shape():
  # make turtle to appear in case its hiden
  turtle.showturtle()
  # play with loop to draw different shapes
  for step in range(6):
    turtle.begin_fill()
    for i in range(3):
      turtle.forward(50)
      turtle.left(360/3)
    turtle.end_fill()
    turtle.forward(50)
    turtle.right(60)

  # hide the turtle
  turtle.hideturtle()



# call the function a few times in a loop
# move a turtle to make a space for a new shape
for i in range(6):
  draw_shape()
  turtle.up()
  turtle.left(300)





