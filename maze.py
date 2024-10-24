map = {
    "room1": {
        "title":"Room 1",
        "loc_x":-620,
        "loc_y":220,
        "width":100,
        "height":100,
        "color":"blue"
    },
    "room2": {
        "title":"Room 2",
        "loc_x":-520,
        "loc_y":280,
        "width":100,
        "height":100,
        "color":"blue"
    },
    "room3": {
        "title":"Room 3",
        "loc_x":-520,
        "loc_y":160,
        "width":100,
        "height":100,
        "color":"blue"
    },
    "room4": {
        "title":"Room 4",
        "loc_x":-420,
        "loc_y":280,
        "width":100,
        "height":100,
        "color":"blue"
    },
    "room5": {
        "title":"Room 5",
        "loc_x":-460,
        "loc_y":60,
        "width":100,
        "height":100,
        "color":"blue"
    },
    "item1": {
        "title":"Pocket",
        "loc_x":620,
        "loc_y":270,
        "width":100,
        "height":100,
        "color":"green"
    },
    "item2": {
        "title":"",
        "loc_x":620,
        "loc_y":170,
        "width":100,
        "height":100,
        "color":"green"
    },
    "item3": {
        "title":"",
        "loc_x":620,
        "loc_y":70,
        "width":100,
        "height":100,
        "color":"green"
    }
}

cur_loc = "room1" # for the agent

key_loc = "room2" # for the key

game_screen = {
    "title":"Screen",
    "text":"Some sample text.",
    "loc_x": 0,
    "loc_y":-250,
    "width":600,
    "height":170,
    "color": "orange"
}

def set_key_loc(loc):
    global key_loc
    key_loc = loc

def get_key_loc():
    global key_loc
    return key_loc

def set_cur_loc(loc):
    global cur_loc
    cur_loc = loc

def get_cur_loc():
    global cur_loc
    return cur_loc

pocket_queue = []
listeners = []