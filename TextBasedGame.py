#Jonathan Ayala
# IT-140

def show_intro(player_name):
    # Intro
    print('Welcome to “Imperial Nightmare,”', player_name + '!', '\n', '---------------------------', '\n',
          'You are an Imperial guardsman traveling back home on a spaceship, with your fellow guardsmen after a five yearlong mission.', '\n',
          'You are in your living quarters, and you suddenly awaken from your sleep realizing half of your crew is dead and the other half is missing.', '\n',
          'You then realize that they are being hunted and captured by a figure known as a Chaos Space Marine.', '\n',
          'To save the rest of your crew and make it back home, you must defeat the Chaos Space Marine in the Command Center.', '\n',
          'To defeat him, first you must retrieve a MAP from the Cafeteria to help you navigate the spaceship.', '\n',
          'A HELMET from the War Room, ARMOR from the Armory, BOLTER AMMO from the Trophy Room, A GRENADE from the LAB, and a BOLTER GUN from the Captain’s Chambers.', '\n',
          'If you do not retrieve all 6 items, the Chaos Space Marine will be too powerful to defeat, and you and your guardsmen will never see home again.', '\n')

#instructions
def show_instructions():
    print('---------------------------', '\n', '*** INSTRUCTIONS ***', '\n',
          'To move, type commands: North, South, East, West', '\n',
          'To add an Item to your inventory, type: get "Item Name"', '\n',
          'To quit the game, type: quit', '\n')


def game_start():
    print('***Start Game***')

def move_between_rooms(current_room, move, rooms):
    return rooms[current_room][move]

def grab_item(current_room, rooms, inventory):
    inventory.append(rooms[current_room]['Item'])
    del rooms[current_room]['Item']

def main():
    # dictionary of Rooms + Items
    rooms = {
        'Living Quarters': {'East': 'Cafeteria'},
        'Cafeteria': {'West': 'Living Quarters', 'North': 'War Room', 'East': 'Trophy Room', 'South': 'Captains Chambers', 'Item': 'Map'},
        'War Room': {'South': 'Cafeteria', 'East': 'Armory', 'Item': 'Helmet'},
        'Armory': {'West': 'War Room', 'Item': 'Armor'},
        'Trophy Room': {'West': 'Cafeteria', 'North': 'Lab', 'Item': 'Bolter Ammo'},
        'Lab': {'South': 'Trophy Room', 'Item': 'Grenade'},
        'Captains Chambers': {'North': 'Cafeteria', 'East': 'Command Center', 'Item': 'Bolter Gun'},
        'Command Center': {'West': 'Captains Chambers'}#Chaos Space Marine
    }

    # List to track inventory
    inventory = []
    # Tracking current room
    current_room = 'Living Quarters'
    # Player name
    player_name = input("Enter player name: ")
    show_intro(player_name)
    show_instructions()
    game_start()

    while True:
        if current_room == 'Command Center':
            # Winning outcome
            if len(inventory) >= 6:
                print('You have successfully defeated the Chaos Space Marine and saved your guardsmen! You can now go home. Congratulations,', player_name + '!')
                print('Thank you for playing Imperial Nightmare!')
                break
            # Losing outcome
            else:
                print('You did not retrieve all items, the Chaos Space Marine is too powerful to defeat. You and your guardsmen will never see home again.')
                print('Thank you for playing Imperial Nightmare! Better luck next time,', player_name + '!')
                break

        print('\nYou are in the', current_room)
        print('Inventory:', ', '.join(inventory) if inventory else '(empty)')

        # Show item in room
        if 'Item' in rooms[current_room]:
            print('You found the {}.'.format(rooms[current_room]['Item']))

        print('---------------------------')
        move = input('Enter command: ').strip()

        if not move:
            print('Invalid command.')
            continue

        words = move.title().split()

        # Movement
        if len(words) == 1 and words[0] in ['North', 'South', 'East', 'West']:
            direction = words[0]
            if direction in rooms[current_room]:
                current_room = move_between_rooms(current_room, direction, rooms)
            else:
                print('You cannot go that way!')
            continue

        # Get item
        elif len(words) >= 2 and words[0] == 'Get':
            item_name = ' '.join(words[1:])
            room_item = rooms[current_room].get('Item', '').lower()
            if item_name.lower() == room_item:
                print('You picked up the {}.'.format(rooms[current_room]['Item']))
                grab_item(current_room, rooms, inventory)
            #item not available
            else:
                print('No such item here.')
            continue

        # Status
        elif move.lower() == 'status':
            print('You are in the', current_room)
            print('Inventory:', ', '.join(inventory) if inventory else '(empty)')
            continue

        # Instructions
        elif move.lower() == 'instructions':
            show_instructions()
            continue

        # Quit
        elif move.lower() in ['quit', 'exit']:
            print('You have quit the game, thank you for playing Imperial Nightmare ' + player_name + '!')
            break
        #invalid commands
        else:
            print('Invalid command.')
            continue

if __name__ == "__main__":
    main()