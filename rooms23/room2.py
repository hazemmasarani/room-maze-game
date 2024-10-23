import turtle

from maze import cur_loc, listeners, game_screen, pocket_queue

from rooms.room1 import room1
from rooms.room4 import room4

from drawer.draw import draw_map

def room2():

    global cur_loc, game_screen
    if cur_loc == "room2":
        game_screen['text'] = """
            Please press the sutable button to change room.
            1) Room 1
            2) Room 4
        """
        cur_loc = "room2"

        for l in listeners:
            turtle.onclick(None, l)

        turtle.onclick(room1, "1")
        listeners.append("1")
        turtle.onclick(room4, "2")
        listeners.append("2")
        pocket_queue.append("key_room5")
    else:
        game_screen['text'] = """
            Please press the sutable button to change room.
            1) Room 1
            2) Room 4
            3) Pick up room 5 key
        """
        cur_loc = "room2"

        for l in listeners:
            turtle.onclick(None, l)

        turtle.onclick(room1, "1")
        listeners.append("1")
        turtle.onclick(room4, "2")
        listeners.append("2")

        draw_map()
    