
rooms = {
    'library': 'The Library: This is the panultimate room for the socially uninclined. Filled with wall-to-ceiling books, loads of natural light, hot tea, and endless cushions, you will never want to leave.',
    'dining room': 'The Dining Room: Come for the food, stay for the people. Furnished with a live-edge dining table and a sizeable wine collection, you will immediately feel at home and ready to eat.',
    'kitchen': 'The Kitchen: Snacks and inspiration galore. The big marble island lets you graze, prep, or pour over an Ottolenghi recipe.',
    'living room': 'The Living Room: Have a sit here on the sectional and play with the pupper before you move on. Maybe a catch an episode of Gilmore Girls while you are at it.'
}

player = {
    'x': 0,
    'y': 2
}

print("You've entered the house, you're currently in the living room.")

while True:
    if (player['x'] == 0 and player['y'] == 2) or (player['x'] == 2 and player['y'] == 0):
        print(rooms['living room'])
    elif (player['x'] == 3 and player['y'] == 0) or (player['x'] == 5 and player['y'] == 2):
        print(rooms['kitchen'])
    elif (player['x'] == 5 and player['y'] == 3) or (player['x'] == 3 and player['y'] == 5):
        print(rooms['dining room'])
    elif (player['x'] == 2 and player['y'] == 5):
        print(rooms['dining room'])
        
    # estbalish directions for user to move
    direction = raw_input("Which direction would you like to move in? N/S/E/W:    ")

    # track how far the user has moved
    if direction == 'N':
        player['y'] += 1
    elif direction == 'S':
        player['y'] -= 1
    elif direction == 'W':
        player['x'] -= 1
    elif direction == 'E':
        player['x'] += 1
    elif direction == "exit":
        print("Goodbye! ")
        break
    # set limits for how far a user can move (ie establish walls)
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
