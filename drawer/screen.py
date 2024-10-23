import turtle

def draw_screen(center_x, center_y, width, height, color, title, text):

    # adjust angle to zero
    turtle.setheading(0)

    # Set the fill color
    turtle.fillcolor(color)
    
    # Start filling the color
    turtle.begin_fill()
    
    # Move the turtle to the starting position
    turtle.penup()
    turtle.goto(center_x - width / 2, center_y - height / 2)
    turtle.pendown()
    
    # Draw the rectangle
    for _ in range(2):
        turtle.forward(width)  # Draw the width
        turtle.left(90)        # Turn left 90 degrees
        turtle.forward(height) # Draw the height
        turtle.left(90)        # Turn left 90 degrees

    # End filling the color
    turtle.end_fill()

    turtle.penup()
    turtle.goto(center_x, center_y + height / 2)  # Position the text inside the rectangle
    turtle.pendown()
    turtle.color('red')  # Set text color
    turtle.write(title, align="center", font=("courier new", 16, "bold"))

    turtle.penup()
    turtle.goto(center_x- 50, center_y - height / 2)  # Position the text inside the rectangle
    turtle.pendown()
    turtle.color('black')  # Set text color
    turtle.write(text, align="center", font=("courier new", 14, "bold"))
