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
#        import Mathgame
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
#    elif current_room == 