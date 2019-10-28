"""
if_adventure.py
 
A text adventure using if/elif statements.
"""
 
# intro/setup
print("Welcome to Ichabod's Text Adventure")
current_room = 'start'
import Welcome
# game loop
while True:
    command = input('\nPress E to continue ')
    # display room contents
    print()
    if current_room == 'start':
        print('Hello and welcome to our game!')
        print('This is where you set off on our epic adventure!')
        if command == 'e':
            current_room = 'math'
    elif current_room == 'math':
        print('Welcome to our math game!')
        print('This is a test of your aptitude in mathematics!')
        import Mathgame
        if command == 'e':
            current_room = "IPCalc"
    elif current_room == 'IPCalc':
        print('This game will test wheter you can find the broadcast address from a given IP and subnet!')
        import ipcalc
        if command == 'e':
            current_room = 'IoT'
    elif current_room == 'IoT':
        print('You are now in the internet of things!')
        print('But alas! There is a quiz!')
        import IoT_Quiz
        if command == 'e':
            current_room = 'Python'
    elif current_room == 'Python':
        print("This game is written in python!")
        print("Let's see what you know about it!")
        import PythonQuiz
        if command == 'e':
            current_room = 'hangman'
    elif current_room == 'hangman':
        print("Oh no! It seems that some is about to be hanged!")
        print("You must save them by guessing a word!")
        print("Notice: This game is PG and will not feature any people getting hanged, 2D or otherwise.")
        import Hangman
        if command == 'e':
            current_room = 'group'
    elif current_room == 'group':
        print("You've made it to our final game!")
        print("Play this game and you can finally be free!")
        if command == 'e':
            current_room = 'end'
    elif current_room == 'end':
        print("You've finished our game!")
        print("Congratzzz fam big up from us")
        break
