"""
if_adventure.py
 
A text adventure using if/elif statements.
"""
 
# intro/setup
print("Welcome to Ichabod's Text Adventure")
current_room = 'start'
 
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
        if command == 'e':
            current_room = "IPcalc"
    elif current_room == 'IPCalc':
        print('You are in a torture chamber.')
        print('There is a rack and an iron maiden against the wall')
        print('and some chains and thumbscrews on the floor.')
    elif current_room == 'bedroom':
        print('You are in a bedroom.')
        print('There is a large bed with black, silk sheets on it.')