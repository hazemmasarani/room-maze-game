import turtle

# Function to draw a agent
def draw_agent(center_x, center_y, color):
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
    turtle.left(90)   
    for _ in range(2):
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(3)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(40) # Draw the height

    turtle.penup()
    turtle.left(180)        # Turn left 90 degrees
    turtle.forward(5)  # Draw the width

    # Draw the rectangle
    turtle.left(130)   
    for _ in range(2):
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(20) # Draw the height

    # Draw the rectangle
    turtle.left(90)   
    for _ in range(2):
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(2)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(20) # Draw the height

    # Draw the rectangle
    turtle.left(130)   
    turtle.forward(35)  # Draw the width
    
    # End filling the color
    turtle.end_fill()