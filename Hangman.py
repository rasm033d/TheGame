#from https://www.youtube.com/watch?v=jPmBUoSZ6tY&feature=share
import random

# list of answers
answerlist = ["oxygen", "denmark", "dinosaur", "coruscant", "squarepants"]
random.shuffle(answerlist) # shuffles the words in the list
answer = list(answerlist[0]) # makes (w, o, r, d)

display = []
display.extend(answer)

for i in range (len(display)):
    display[i] = ""             # turns letters into "__"
print(" " .join(display))        # makes spaces "      "
print()

count = 0

while count < (len(answer)):
    guess = str(input("guess a letter: "))
    guess = guess.lower()        # makes a guess in lower cases
    # print(count)


    for i in range(len(answer)):
        if answer[i] == guess:   # if a letter is guessed
            display[i] = guess   # turn "_" into a "letter"
            count += 1           # count raises


    print(" " .join(display))
    print()
print("Well done you guessed the word")
