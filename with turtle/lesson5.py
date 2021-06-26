import turtle

# initialize the turtle and the app interface
turtle.shape('turtle')

# adjust the turtle size
turtle.shapesize(1)

# adjust the color
turtle.color('red','blue')

# init screen and pen 
window = turtle.Screen()

# define a function to make turtle follow the user click
def turtle_headto(x, y):
    turtle.left(turtle.towards(x, y) - turtle.heading())
    turtle.goto(x, y)



# make a reaction on mouse click
window.onscreenclick(turtle_headto)

# make the screen listen for updates and run constantly
window.listen()
window.mainloop()