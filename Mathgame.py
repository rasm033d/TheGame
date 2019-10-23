import random
import operator

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2,)
    print(f'What is {num_1} {operation} {num_2}?')

    return answer

def ask_question():
    answer = random_problem()
    guess = float(input())
    return guess == answer

def game():
    print("How well do you know math?\n")
    score = 0
    for i in range(10):
        if ask_question() == True:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print(f'Your score is {score}')

game()
