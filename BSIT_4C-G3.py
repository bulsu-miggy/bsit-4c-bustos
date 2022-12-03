import random
import group_3_questions #FILE NAME KUNG ASAN MGA QUESTIONS

print("INSTRUCTION: Just input the letter of your answer. \n")

random.shuffle(group_3_questions.questions)
User_scores = 0

#FOR CHECKING IF THE ANSWER IS CORRECT OR NOT
for i in range(0, len(group_3_questions.questions), 1):
    User_answer = input(group_3_questions.questions[i][0])
    if User_answer.lower() == group_3_questions.questions[i][1].lower():
        print("Correct")
        User_scores += 1
    else:
        print("Wrong!")

#FOR SINGULAR OR PLURAL OF PRINTING SCORES :>
if User_scores > 1:
    print("You've got " + str(User_scores) + " correct answers.")
else:
    print("You've got " + str(User_scores) + " correct answer.")