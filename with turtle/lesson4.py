import turtle

# initialize the turtle and the app interface
turtle.shape('turtle')

# adjust the turtle size
turtle.shapesize(1)

# adjust the color
turtle.color('red','blue')

# init screen and pen 
window = turtle.Screen()

# define a function to move turtle up
def moveUp():
  # init coordinates
  x = turtle.position()[0]
  y = turtle.position()[1]
  # turn turtle up
  turtle.setheading(90)
  # make a move
  turtle.setposition(x, y+5)
  
# make a reaction on keybord input
window.onkey(moveUp, 'Up')


# make the screen listen for updates and run constantly
window.listen()
window.mainloop()