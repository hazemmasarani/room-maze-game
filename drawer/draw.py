import turtle

from maze import map, cur_loc, key_loc

from drawer.room import draw_room
from drawer.agent import draw_agent
from drawer.key import draw_key

# Function to clear the screen
def clear_map():
    turtle.clear()  # Clear the drawn shapes
    turtle.penup()  # Lift the pen so it doesn't draw while moving
    turtle.home()   # Move the turtle to the starting position

def draw_map():

    clear_map()

    for room_name in map:
        room = map[room_name]
        draw_room(room['loc_x'], room['loc_y'], room['width'], room['height'], room['color'], room['title'])

    cur_room = map[cur_loc]

    draw_agent(cur_room['loc_x'], cur_room['loc_y'], "black")

    key_room = map[key_loc]
    draw_key(key_room['loc_x'], key_room['loc_y'])