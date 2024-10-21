import turtle

def draw_key(x,y):
    x += 30
    y -= 10
    # adjust angle to zero
    turtle.setheading(90)

    # Move to the starting position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the head of the key
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(10)  # Circle for the head

    # Draw the shaft of the key
    turtle.goto(x + 5, y - 20)  # Move down for the shaft

    turtle.pendown()
    turtle.forward(40)  # Length of the shaft


    # Draw the teeth of the key
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)

    turtle.left(90)
    turtle.forward(15)

    turtle.left(45)
    turtle.forward(40)

    turtle.right(30)
    turtle.forward(20)

    turtle.goto(x + 5, y - 20)

    turtle.end_fill()

    # # Return to the starting position
    # turtle.penup()
    # turtle.goto(x + 60, y)  # Adjust for the next key
    # turtle.pendown()



