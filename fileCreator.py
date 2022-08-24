import json

questions = {"1": "What year did man land on the moon?",
             "2": "Which Indonesian island shares a name with a programming language? ",
             "3": "What is the formula for water? ",
             "4": "The UV in UV rays stand for what? ",
             "5": "Which currency was used in italy prior to the Euro? ",
             "6": "Where was the croissant invented? ",
             "7": "Which movie won the first Oscar for best picture? ",
             "8": "What musical piece was Mozart's last? ",
             "9": "What country was Stalin born? ",
             "10": "Who separated the red sea in the old testament? "}


with open("question.txt", "w") as question_file:
    question_file.write(json.dumps(questions))
'''
answers = {"1": "1969",
           "2": "java",
           "3": "h2o",
           "4": "ultraviolet",
           "5": "lira",
           "6": "austria",
           "7": "wings",
           "8": "requiem",
           "9": "georgia",
           "10": "moses"
           }

with open("answers.txt", "w") as answers_file:
    answers_file.write(json.dumps(answers))
'''