# Code block under is my own code, before I got stuck at trying to avoid having question duplicates.

'''
answer = input("Are you ready to play the quiz? (yes/no) :")
name = input(f"\nWhat's your name? ")
points = 0
total_questions = 10

while total_questions <= 10:
    if answer.lower() == "yes":
        question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(len(question)):
            answers = input(f"Question " + str(question[i]) + ": " + random.choice(list(qdic.values())))
            givenAnswer = answers
            if givenAnswer.lower() in adic.values():
                points += 1
                print("Correct!")

            else:
                print("Wrong answer =(")
            i += 1


    total_questions += 1

print(f"Thank you for playing {name}, you answered {points} out of 10 questions correctly!")
score = {name.capitalize(): points}
print(f"Points obtained: {score}")


with open("results.txt", "w") as results_file:
    results_file.write(json.dumps(score))
'''