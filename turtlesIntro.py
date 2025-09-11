import turtle

# Create a screen and a turtle object

#creating a variable tat will store the screen object
#turtle.Screen you are sinstantianing a Screen object

#data types that are objects normally have a behavior attached to it
#behaviors are functions or methods

screen = turtle.Screen()
screen.title("Turtle Example in Python")

# Create a turtle instance - instantiating a Turtle object
my_turtle = turtle.Turtle()

# Draw a square
# for loop will loop through the same code 4 times 
# the i represends the loop variable 

for i in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
closeWindow = input("Press any key to close window. ")
screen.mainloop()

# Keep the window open until clicked
turtle.done()