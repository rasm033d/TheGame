#https://python-forum.io/Thread-Text-Adventure-Tutorial-if-structure-to-dictionary
#Skeleton structure of the way the rooms will work, i.e. where the games are.
#TODO: Add enough rooms for all the games, find a way to visually represent where the player is in relation to the world map, fix the player representation on the map, and add more
import ipcalc
"""
if_adventure.py
 
A text adventure using if/elif statements.
"""
 
# intro/setup
print("To Group 5's game!")
current_room = 'start'
 
# game loop
while True:
    # display room contents
    print()
    if current_room == 'start':
        print("|[ ][ ][ ]|")
        print("|[ ][ ][ ]|")
        print("|[ ][^][ ]|")
        print('This is the start room!')
        print("This is where you will be able to decide where you go")
    elif current_room == 'Math':
        print("|[ ][ ][ ]|")
        print("|[ ][^][ ]|")
        print("|[ ][ ][ ]|")
        print('This is where the math game will be')
        print('Need to figure out how to load it into this')
        ipcalc
    elif current_room == 'hangman':
        print("|[ ][^][ ]|")
        print("|[ ][ ][ ]|")
        print("|[ ][ ][ ]|")
        print('You are in the hangman chamber.')
        print('Load it in')
    elif current_room == 'subnet':
        print("|[ ][ ][^]|")
        print("|[ ][ ][ ]|")
        print("|[ ][ ][ ]|")
        print('Subnet challenge')
        print('Load it in')
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command.lower() in ('n', 'north'):
        if current_room == 'start':
            current_room = 'Math'
        elif current_room == 'subnet':
            current_room = 'hangman'
        else:
            print("You can't go that way.")
    elif command.lower() in ('s', 'south'):
        if current_room == 'Math':
            current_room = 'start'
        elif current_room == 'hangman':
            current_room = 'subnet'
        else:
            print("You can't go that way.")
    elif command.lower() in ('e', 'east'):
        if current_room == 'start':
            current_room = 'subnet'
        elif current_room == 'Math':
            current_room = 'hangman'
        else:
            print("You can't go that way.")
    elif command.lower() in ('w', 'west'):
        if current_room == 'subnet':
            current_room = 'start'
        elif current_room == 'hangman':
            current_room = 'Math'
        else:
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    else:
        print("I don't understand that command.")