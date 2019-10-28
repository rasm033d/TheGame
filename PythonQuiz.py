#import Question
import random
import operator
import time

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is a correct syntax to output 'Hello World' in Python?\n(a) print('Hello World')\n(b) echo('Hello World')\n(c) p('Hello World')\n\n",
    "How do you insert COMMENTS in Python code?\n(a) #This is a comment\n(b) //This is a comment\n(c) /*This is a comment*/\n\n",
    "Which one is NOT a legal variable name?\n(a) my_var\n(b) Myvar\n(c) my-var\n\n",
    "What is the correct way to create a function in Python?\n(a) function myfunction():\n(b) def myFunction():\n(c) create myFunction():\n\n"
]

questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" +str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
#print(" STARTING   MATH   GAME . . . ")
#time.sleep(4)
#print(" GET READY")
#time.sleep(1) 
#def random_problem():
#    operators = {
#        '+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#
#
#    num_1 = random.randint(1, 1000)
#   num_2 = random.randint(1, 1000)
#    operation = random.choice(list(operators.keys()))
#    answer = operators.get(operation)(num_1, num_2,)
#   print(f'What is {num_1} {operation} {num_2}?')
#
#    return answer
#
#def ask_question():
#    answer = random_problem()
#    guess = int(input())
#    return guess == answer
#
#def game():
#    print("How well do you know math?\n")
#    score = 0
#    for i in range(6):
#        if ask_question() == True:
#            score += 1
#            print("Correct!")
#        else:
#            print("Incorrect!")
#
#
#   print(f'Your score is {score}')
#game()
