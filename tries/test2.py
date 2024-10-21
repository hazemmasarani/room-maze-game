import turtle

def draw_rectangle(center_x, center_y, width, height, color):
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

# Example usage
turtle.speed(90000)  # Set the drawing speed
draw_rectangle(0, 0, 100, 50, 'green')  # Draw a blue rectangle
draw_rectangle(100, 100, 100, 50, 'blue')  # Draw a blue rectangle
draw_rectangle(-100, -100, 100, 50, 'red')  # Draw a blue rectangle
draw_rectangle(-100, 100, 100, 50, 'yellow')  # Draw a blue rectangle
draw_rectangle(100, -100, 100, 50, 'black')  # Draw a blue rectangle
turtle.done()    # Finish the drawing
