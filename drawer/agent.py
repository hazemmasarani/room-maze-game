import turtle

# Function to draw a agent
def draw_agent(center_x, center_y, color):
    turtle.penup()
    # Set the fill color
    turtle.fillcolor(color)
    
    # Start filling the color
    turtle.begin_fill()
    
    # Move the turtle to the starting position
    turtle.penup()
    turtle.goto(center_x, center_y + 15)  # Position turtle at the bottom of the circle
    turtle.pendown()
    
    # Draw the circle
    turtle.circle(15)

    # Draw the rectangle
    turtle.right(90)  

    for _ in range(2):
        turtle.forward(40)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(3) # Draw the height
        turtle.left(90)        # Turn left 90 degrees
    
    turtle.penup()
    turtle.forward(5)  # Draw the width

    # Draw the rectangle
    turtle.right(30)   
    turtle.pendown()
    for _ in range(2):
        turtle.forward(20)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2) # Draw the height
        turtle.left(90)        # Turn left 90 degrees

    turtle.left(60) 

    # Draw the rectangle
    for _ in range(2):
        turtle.forward(20)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2) # Draw the height
        turtle.left(90)        # Turn left 90 degrees

    turtle.penup()
    turtle.right(30)  
    turtle.forward(35)
    turtle.left(30)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(20)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2) # Draw the height
        turtle.left(90)        # Turn left 90 degrees

    turtle.penup()
    turtle.right(60)
    turtle.pendown()
    
    for _ in range(2):
        turtle.forward(20)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2) # Draw the height
        turtle.left(90)        # Turn left 90 degrees

    turtle.penup()

    turtle.right(150)
    turtle.forward(40)

    # End filling the color
    turtle.end_fill()