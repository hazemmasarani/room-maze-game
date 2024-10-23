import turtle

from maze import map, cur_loc, key_loc, game_screen, get_cur_loc, get_key_loc

from drawer.room import draw_room
from drawer.agent import draw_agent
from drawer.key import draw_key
from drawer.screen import draw_screen
from drawer.pocket import draw_pocket

# Function to clear the screen
def clear_map():
    turtle.clear()  # Clear the drawn shapes
    turtle.penup()  # Lift the pen so it doesn't draw while moving
    turtle.home()   # Move the turtle to the starting position

def draw_map():
    cur_loc = get_cur_loc()
    key_loc = get_key_loc()
    clear_map()

    for room_name in map:
        room = map[room_name]
        draw_room(room['loc_x'], room['loc_y'], room['width'], room['height'], room['color'], room['title'])

    cur_room = map[cur_loc]

    draw_agent(cur_room['loc_x'], cur_room['loc_y'], "black")

    draw_screen(game_screen['loc_x'], game_screen['loc_y'], game_screen['width'], game_screen['height'], game_screen['color'], game_screen['title'], game_screen['text'])

    # for item in pocket_boxs:
    #     box = pocket_boxs[item]
    #     draw_pocket(box['loc_x'], box['loc_y'], box['width'], box['height'], box['color'], box['title'])

    key_room = map[key_loc]
    draw_key(key_room['loc_x'], key_room['loc_y'])
