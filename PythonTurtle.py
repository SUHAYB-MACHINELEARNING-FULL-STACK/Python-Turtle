from turtle import * # I'm going to import the turtle for using this turtle
OrderRibs = input("Ribs Count: ") # We ask the user to count the number of sides for the shape they want
OrderColor = input("Color: ") # We ask the user to put the color of the shape he wants
OrderWidth = input("Width: ") # We ask the user to width the look he wants
OrderForward = input("Forward: ") # We ask the user to set how far the turtle is facing forward on each side

color(OrderColor) # Here I have selected the color for the shape according to the data entered by the user
width(int(OrderWidth)) # Here I have selected the width of All side
hideturtle() # Here I have hidden the turtle, which is an arrow, so nothing will be visible but the ribs while it is drawing
for i in range(int(OrderRibs)): # Here I created a rotation sentence that follows a pattern from zero to the number of sides created by the user -- Note: the user put the number of sides but it remains a string so I converted it to an integer
    forward(OrderForward) # Here I have selected the Forward for the shape according to the data (Data of the user)
    left(180 - (((int(OrderRibs)-2)*180)/int(OrderRibs))) # Here I have determined the extent to which the side is pointing to the left each time so that the sides are equal by establishing the equilateral law
