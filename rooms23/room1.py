import turtle

from maze import cur_loc, listeners, game_screen

from rooms.room2 import room2
from rooms.room3 import room3

from drawer.draw import draw_map

def room1():
    game_screen['text'] = """
        You need to enter room 5 to win the game. If you entered room 4 you will lose.

        Please press the sutable button to change room.
        1) Room 2
        2) Room 3
    """
    
    global cur_loc
    cur_loc = "room1"

    for l in listeners:
        turtle.onclick(None, l)

    turtle.onclick(room2, "1")
    listeners.append("1")
    turtle.onclick(room3, "2")
    listeners.append("2")

    draw_map()

    