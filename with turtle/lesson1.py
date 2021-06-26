import turtle

# initialize the turtle and the app interface
turtle.shape('turtle')

# adjust the turtle size
turtle.shapesize(2)

# adjust the color
turtle.color('red')

# play with loop to draw different shapes
for step in range(6):
  turtle.forward(50)
  turtle.right(60)

# hide the turtle
turtle.hideturtle()
