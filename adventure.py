
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

def adjust_position(direction):
    if direction == "E":
        player['x'] -= 1
    if direction == "W":
        player['x'] += 1
    elif direction == 'N':
        player['y'] -= 1
    elif direction == 'S':
        player['y'] += 1

def check_walls(direction):
    # Living Room logic
    if player['current room'] == 'living room':
        if (player['x'] == 0 and player['y'] == 2) or (player['x'] == 2 and player['y'] == 0):
            player['current room'] = 'living room'
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(rooms['living room'])
            print('~~~~~~~~~~~~~~~~~~~~~~~')
        elif (player['x'] == 3 and player['y'] == 0):
            player['current room'] = 'kitchen'
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(rooms['kitchen'])
            print('~~~~~~~~~~~~~~~~~~~~~~~')
        elif (player['y'] > 2 or player['x'] > 2):
            print('You cannot move further in this direction.')
            adjust_position(direction)

    # Kitchen Logic
    elif player['current room'] == 'kitchen':
        if (player['x'] == 3 and player['y'] == 0) or (player['x'] == 5 and player['y'] == 2):
            player['current room'] = 'kitchen'
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(rooms['kitchen'])
            print('~~~~~~~~~~~~~~~~~~~~~~~')
        elif player['x'] == 2 and player['y'] == 0:
            player['current room'] = 'living room'
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(rooms['living room'])
            print('~~~~~~~~~~~~~~~~~~~~~~~')
        elif player['x'] == 5 and player['y'] == 3:
            player['current room'] = 'dining room'
            print('~~~~~~~~~~~~~~~~~~~~~~~')
            print(rooms['dining room'])
            print('~~~~~~~~~~~~~~~~~~~~~~~')
        elif (player['y'] > 2 or player['x'] > 6) :
            print('You cannot move further in this direction.')
            adjust_position(direction)

    # Dining Room Logic
    elif (player['y'] > 5 or player['x'] > 6) and player['current room'] == 'dining room':
        print('You cannot move further in this direction.')
        return True

    # Library Logic
    elif (player['y'] > 5 or player['x'] > 2) and player['current room'] == 'library':
        print('You cannot move further in this direction.')
        return True

def at_door():
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
        check_walls(direction)
    elif direction == 'S':
        player['y'] -= 1
        check_walls(direction)
    elif direction == 'W':
        player['x'] -= 1
        check_walls(direction)
    elif direction == 'E':
        player['x'] += 1
        check_walls(direction)
    elif direction == "exit":
        print("Goodbye! ")
        break

    print(player)
