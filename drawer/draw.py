from maze import map, cur_loc

from drawer.room import draw_room
from drawer.agent import draw_agent

def draw_map():
    for room_name in map:
        room = map[room_name]
        draw_room(room['loc_x'], room['loc_y'], room['width'], room['height'], room['color'], room['title'])

    cur_room = map[cur_loc]

    draw_agent(room['loc_x'], room['loc_y'], "black")
    