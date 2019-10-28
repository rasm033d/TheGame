score = 0
print ("Welcome to the IoT Quiz")
print (" ")
begin = input ("Would you like to begin?:")
print (" ")
if begin == "yes":
    print ("A) Lm35")
    print ("B) HCSR04")
    print ("C) MQ2Gas")
    Question1 = input ("What is the name of the sensor you use for temperature?: ")
    if Question1 == "A" or Question1 == "a":
        print ("Correct!")
        print (" ")
        score += 1
    else:
        print ("Wrong answer!")
    print ("A) 240 Ohm")
    print ("B) 220 Ohm")
    print ("C) 330 Ohm")
    Question2 = input ("What kind of resistor do you need to have on an Arduino if you have a LED?: ")
    if Question2 == "B" or Question2 == "b":
        print ("Correct!")
        print (" ")
        score += 1
    else:
        print ("Wrong answer!")
    print ("A) 8 bits")
    print ("B) 16 bits")
    print ("C) 24 bits")
    Question3 = input ("How many bits are in a bite?: ")
    if Question3 == "a" or Question3 == "A":
        print ("Correct!")
        print (" ")
        score += 1
    else:
        print ("Wrong answer!")
    print ("A) 64 bits")
    print ("B) 32 bits")
    print ("C) 128 bits")
    Question4 = input ("What size is IPv6 address?: ")
    if Question4 == "c" or Question4 == "C":
        print ("Correct!")
        score += 1
    else:
        print ("Wrong answer!")
        print (" ")
    print ("A) 64 bits")
    print ("B) 32 bits")
    print ("C) 128 bits")
    Question5 = input ("What size is IPv4 address?: ")
    if Question5 == "b" or Question5 == "B":
        print ("Correct!")
        score += 1
    print ("Your score is", str(score) + "/5 Correct!")
else:
        print ("Thanks for trying our IoT Quiz")
