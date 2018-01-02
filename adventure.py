
rooms = {
    'library': 'The Library: This is the panultimate room for the socially uninclined. Filled with wall-to-ceiling books, loads of natural light, hot tea, and endless cushions, you will never want to leave.',
    'dining room': 'The Dining Room: Come for the food, stay for the people. Furnished with a live-edge dining table and a sizeable wine collection, you will immediately feel at home and ready to eat.',
    'kitchen': 'The Kitchen: Snacks and inspiration galore. The big marble island lets you graze, prep, or pour over an Ottolenghi recipe.',
    'living room': 'The Living Room: Have a sit here on the sectional and play with the pupper before you move on. Maybe a catch an episode of Gilmore Girls while you are at it.'
}

player = {
    'x': 0,
    'y': 2,
    'current room': 'living room'
}


print("You've entered the house, you're currently in the living room.")

def check_walls():
    if player is y  == 0 and x == 2
    if player['current room'] == 'living room':
        if (player['y'] > 2 or player['x'] > 2):
            print('You cannot move further in this direction.')
            return True
        else:
            at_door()
    elif player['current room'] == 'kitchen':
        if (player['y'] > 2 or player['x'] > 6) :
            print('You cannot move further in this direction.')
            return True
        else:
            at_door()
    elif (player['y'] > 5 or player['x'] > 6) and player['current room'] == 'dining room':
        print('You cannot move further in this direction.')
        return True
    elif (player['y'] > 5 or player['x'] > 2) and player['current room'] == 'library':
        print('You cannot move further in this direction.')
        return True

def at_door():
    if (player['x'] == 0 and player['y'] == 2) or (player['x'] == 2 and player['y'] == 0):
        player['current room'] = 'living room'
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(rooms['living room'])
        print('~~~~~~~~~~~~~~~~~~~~~~~')
    elif (player['x'] == 3 and player['y'] == 0) or (player['x'] == 5 and player['y'] == 2):
        player['current room'] = 'kitchen'
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(rooms['kitchen'])
        print('~~~~~~~~~~~~~~~~~~~~~~~')
    elif (player['x'] == 5 and player['y'] == 3) or (player['x'] == 3 and player['y'] == 5):
        player['current room'] = 'dining room'
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(rooms['dining room'])
        print('~~~~~~~~~~~~~~~~~~~~~~~')
    elif (player['x'] == 2 and player['y'] == 5):
        player['current room'] = 'library'
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(rooms['library'])
        print('~~~~~~~~~~~~~~~~~~~~~~~')

while True:

    # estbalish directions for user to move
    direction = raw_input("Which direction would you like to move in? N/S/E/W:    ")

    # track how far the user has moved
    if direction == 'N':
        player['y'] += 1
        at_door()
        if check_walls():
            player['y'] -= 1
    elif direction == 'S':
        player['y'] -= 1
        at_door()
        if check_walls():
            player['y'] += 1
    elif direction == 'W':
        player['x'] -= 1
        at_door()
        if check_walls():
            player['x'] += 1
    elif direction == 'E':
        at_door()
        player['x'] += 1
        if check_walls():
            player['x'] -= 1
    elif direction == "exit":
        print("Goodbye! ")
        break

    print(player)

#
# living room, x =  0, 1, 2
# living room, y =  0, 1, 2
# kitchen, x     =  3, 4, 5, 6
# ktichen, y     =  0, 1, 2
#
# dining room, x =  3, 4, 5, 6
# dining room, y =  3, 4, 5
# library, x     =  0, 1, 2
# library, y     =  3, 4, 5
