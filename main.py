import random
import ast
import json

# Reading from question and answers from respective files.
with open("question.txt", "r") as questions:
    qdic = ast.literal_eval(questions.read())

with open("answers.txt", "r") as answers:
    adic = ast.literal_eval(answers.read())

# Introduction message
print("Welcome to my quiz!")

# Opening statement and inputs from user.
answer = input("Are you ready to play the quiz? (yes/no) :")
if answer.lower() == "yes":
    name = input(f"\nWhat's your name? ")
    points = 0

# Code beneath edited and tidied up with help from Quamrana at Stackoverflow.
    question_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(question_numbers)

    for i,q in enumerate(question_numbers):
        question = qdic[str(q)]
        response = input(f"Question {i+1}: {question}").lower()
        answer = adic[str(q)].lower()
        if response == answer:
            points += 1
            print("Correct!")
        else:
            print("Wrong answer =(")
    print(f"Thank you for playing {name}, you answered {points} out of 10 questions correctly!")
    score = {name.capitalize(): points}
    with open("results.txt", "w") as results_file:
        results_file.write(json.dumps(score))


