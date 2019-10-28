#https://python-forum.io/Thread-Text-Adventure-Tutorial-if-structure-to-dictionary
#Skeleton structure of the way the rooms will work, i.e. where the games are.
#TODO: Add enough rooms for all the games, find a way to visually represent where the player is in relation to the world map, fix the player representation on the map, and add more
from ipcalc import winconIP
"""
if_adventure.py
 
A text adventure using if/elif statements.
"""
 
# intro/setup
print("Welcome to Group 5's game!")
current_room = 'start'

if current_room == 'start':
    print("|[ ][ ][ ]|")
    print("|[ ][ ][ ]|")
    print("|[ ][^][ ]|")
    print('This is the start room!')
    print("This is where you will be able to decide where you go")
    answerkey = input("Do you want to play our game? Press E ")
    if answerkey == 'e':
        current_room = "Math"
elif current_room == 'Math':
        print("|[ ][ ][ ]|")
        print("|[ ][^][ ]|")
        print("|[ ][ ][ ]|")
        print('This is where the math game will be')
        print('Need to figure out how to load it into this')
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