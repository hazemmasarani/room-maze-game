import turtle

from maze import listeners, game_screen, pocket_queue, get_cur_loc, set_cur_loc, set_key_loc, get_key_loc

from drawer.draw import draw_map

# Set up the screen
screen = turtle.Screen()
screen.listen() 

def room1():
    global game_screen, pocket_queue, listeners

    game_screen['text'] = """
        You need to enter room 5 to win the game.
        If you entered room 4 you will lose.

        Please press the sutable button to change room.
        1) Room 2
        2) Room 3
    """
    
    set_cur_loc( "room1")

    for l in listeners:
        screen.onkey(None, l)

    screen.onkey(room2, "1")
    listeners.append("1")
    screen.onkey(room3, "2")
    listeners.append("2")
    draw_map()

def room2():
    global game_screen, pocket_queue, listeners
    set_cur_loc("room2")

    for l in listeners:
        screen.onkey(None, l)

    screen.onkey(room1, "1")
    listeners.append("1")
    screen.onkey(room4, "2")
    listeners.append("2")

    if get_key_loc() != "room2" :
        game_screen['text'] = """
            Please press the sutable button to change room.
            1) Room 1
            2) Room 4
        """
    else:
        game_screen['text'] = """
            Please press the sutable button to change room.
            1) Room 1
            2) Room 4
            3) Pick up room 5 key
        """
        screen.onkey(pick_room_5_key, "3")
        listeners.append("3")

    draw_map()

def pick_room_5_key():
    
    game_screen['text'] = """
        Please press the sutable button to change room.
        1) Room 1
        2) Room 4
    """
    set_cur_loc( "room2")
    set_key_loc("item1")

    for l in listeners:
        screen.onkey(None, l)

    screen.onkey(room1, "1")
    listeners.append("1")
    screen.onkey(room4, "2")
    listeners.append("2")
    pocket_queue.append("key_room5")
    
    draw_map()

def room3():
    global game_screen, pocket_queue, listeners

    game_screen['text'] = """
        Please press the sutable button to change room.
        1) Room 1
        2) Room 5
    """
    
    set_cur_loc( "room3")

    for l in listeners:
        screen.onkey(None, l)

    screen.onkey(room1, "1")
    listeners.append("1")
    screen.onkey(room5, "2")
    listeners.append("2")
    draw_map()

def room4():
    global game_screen, pocket_queue, listeners

    game_screen['text'] = """
        Gameover!! you entered room4.
    """
    
    set_cur_loc( "room4")

    for l in listeners:
        screen.onkey(None, l)

    draw_map()

def room5():
    global game_screen, pocket_queue, listeners

    if get_key_loc() == "item1":
        game_screen['text'] = """
            Congratulations!! You win.
        """
        
        set_cur_loc( "room5")

        for l in listeners:
            screen.onkey(None, l)
    else:
        if "You need to find the key to open the door." not in game_screen['text']:
            game_screen['text'] += """
                You need to find the key to open the door.
            """
    draw_map()
