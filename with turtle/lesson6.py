
import turtle
import urllib.request
from PIL import Image

# download and save image
urllib.request.urlretrieve("http://24.media.tumblr.com/tumblr_mdywf7fB651rgpyeqo1_500.gif","myshape.gif")
# resize the image and save 
img = Image.open("myshape.gif") 
img_small = img.resize((28, 28), Image.ANTIALIAS)
img_small.save("myshape.gif")

# initialize the turtle and custom shape
turtle.register_shape(name='myshape.gif')
turtle.shape('myshape.gif')

# adjust the turtle size
turtle.shapesize(0.001)

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