import os
import random
import time
import math
import sys

def countdownText(time_counter, text, end):

    while time_counter:
        mins, secs = divmod(time_counter, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(text, timer, end="...\r")
        time.sleep(1)
        time_counter -= 1

    os.system('cls')
    # print("HERE WE GO...")    

def answer_question(questionnaire):

    question = questionnaire.get("question")
    choices = questionnaire.get("choices")
    correct_answer = questionnaire.get("correct_answer").lower()

    choices_in_texts = format_choices(choices)

    print("Question: " + question)
    for text in choices_in_texts:
        print(text)

    print(112 * "=")
    answer = input("Answer: ").lower()
    
    if answer == "":
        print("You didn't input any answer. It will be considered as", end=" ")
    elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
        print("Your answer seems to be not in the available choices. It will be considered as", end=" ")


    return answer == correct_answer


def format_choices(choices):

    texts = []

    size = len(choices)
    mid_number = math.ceil(size / 2)
    for i in range(0, mid_number):
        letter = list(choices)[i]
        answer_description = list(choices.values())[i]
        answer_text = letter + ". " + answer_description
        
        if (i + mid_number >= size):
            text = answer_text
        else:
            second_letter = list(choices)[i + mid_number]
            second_answer_description = list(choices.values())[i + mid_number]
            second_answer_text = second_letter + ". " + second_answer_description
            text = answer_text + "\t" + second_answer_text

        texts.append(text)
        
    return texts

def aboutUI():
    os.system("cls")

    group_leader = "Chrisler DL. Matucinio"
    members = [
        "Jeffrey S. Tabao",
        "Benjie O. Gapasin",
        "Julius Mari G. Chan",
        "Gem D. Balbastro",
        "Ian Paul E. Fajardo"
    ]

    print(112 * "=")
    print("Created By Group 2 BSIT 4C S.Y. 2022 - 2023")
    print("A Midterm Project in Python Programming Subject")
    print(112 * "=")
    print("Group Leader:\t", group_leader)
    print("Group Members:", end=" ")
    for member in members:
        if member == members[0]:
            print(" ", member)
        else:
            print("\t\t", member)
    print(112 * "=")

    os.system("pause")


while True:
    os.system("cls") 
    print(112 * "=")   
    print("***QUIZ GAME BY GROUP 2***")
    print(112 * "=") 
    print("This is a game that throws 10 random questions about the basic concepts of Python.")
    print("Be prepared because you did not know what you entered.")
    print("SET YOUR MINDS, FACE YOUR FEARS AND KICK THIS ASS OFF!")
    print(112 * "=")
    print("")
    print("MENU") 
    print("a. Start")
    print("b. About")
    print("c. Quit")

    select = input("Select: ")
    select = select.lower()
    
    if (select == "a"):
        break
    elif (select == "b"):
        aboutUI()
    elif (select == "c"):
        os.system("cls")
        print(112 * "=")
        print("Goodbye! Please come back again!!")
        print(112 * "=")
        time.sleep(3)
        os.system('cls')
        sys.exit()
    else:
        print("")
        print("Invalid Command!")
        print("Refreshing page in 3 seconds...")
        time.sleep(3)


os.system("cls")
countdownText(5, "Let's get started in", end="...\r")


print(112 * "=")
print("HERE WE GO...")
print(112 * "=")
time.sleep(2)

score = 0
questionnaires = [ 
    {
        "question" : "It is a kind of loop that repeatedly executes a target statement as long as a given condition is true.",
        "choices" : {"a" : "For Loop", "b" : "While Loop", "c" : "Do Loop", "d" : "Break Loop"},
        "correct_answer" : "b" 
    },
    {
        "question" : "It is a reserved word for loops that terminates the current loop and resumes execution at the next statement.",
        "choices" : {"a" : "continue", "b" : "break", "c" : "pass", "d" : "fail"},
        "correct_answer" : "b" 
    },
    {
        "question" : "It can be used both in while loops and for loops.",
        "choices" : {"a" : "fail and continue", "b" : "break and pass", "c" : "break and continue", "d" : "fail and break"},
        "correct_answer" : "c" 
    },
    {
        "question" : "A statement in Python that is a null operation; nothing happens when it executes.",
        "choices" : {"a" : "continue", "b" : "break", "c" : "pass", "d" : "fail"},
        "correct_answer" : "c" 
    },
    {
        "question" : "A loop that is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).",
        "choices" : {"a" : "For Loop", "b" : "While Loop", "c" : "Do Loop", "d" : "Break Loop"},
        "correct_answer" : "a" 
    },
    {
        "question" : "It is a statement in Python that returns the control to the beginning of the while loop.",
        "choices" : {"a" : "continue", "b" : "break", "c" : "pass", "d" : "fail"},
        "correct_answer" : "a" 
    },
    {
        "question" : "This is a kind of operator that is used to test if a sequence is presented in an object.",
        "choices" : {"a" : "Arithmetic Operator", "b" : "Logical Operator", "c" : "Assignment Operator", "d" : "Membership Operator"},
        "correct_answer" : "d" 
    },
    {
        "question" : "It works more like an iterator method as found in other object-orientated programming languages.",
        "choices" : {"a" : "For Loop", "b" : "While Loop", "c" : "Do Loop", "d" : "Break Loop"},
        "correct_answer" : "a" 
    },
    {
        "question" : "A statement in Python that is used when a statement is required syntactically but you do not want any command or code to execute.",
        "choices" : {"a" : "continue", "b" : "break", "c" : "pass", "d" : "fail"},
        "correct_answer" : "c" 
    },
    {
        "question" : "These are the Membership Operators for For Loops in Python.",
        "choices" : {"a" : "here and not here", "b" : "in and not in", "c" : "present and not present", "d" : "if and else"},
        "correct_answer" : "b" 
    }
]

random.shuffle(questionnaires) 


question_count = 1
for question in questionnaires:
    os.system('cls')

    print(112 * "=")
    print("No. " + str(question_count) + "/" + str(len(questionnaires)))
    print(112 * "=")
    isAnswerCorrect = answer_question(question)
    

    if (isAnswerCorrect):
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
    
    question_count += 1
    time.sleep(2)


# print(60 * "=")
os.system('cls')
print(112 * "=")
print("You just finished the game! That's already incredible!")
print(112 * "=")
countdownText(5, "Tallying your score in ", end="...\r")


os.system('cls')

print(112 * "=")
print("Your Score: " + str(score) + "/" + str(len(questionnaires)))
    # percentage = score / len(questionnaires) * 100
percentage = score / len(questionnaires)
print(112 * "=")
print("Percentage: " + f"{percentage:.0%}")
print(112 * "=")

congrats = "Congratulations!"

if score == 0:
    print("Hilarious!")
    print("\n-This is impossible! Try to play the game again!-")
elif score > 0 and score < 4:
    print("Oh my God!")
    print("\n-Not a good score but it will improve!-")
elif score == 5:
    print(congrats)
    print("\n-You attained the passing score! Keep up the good work!-")
elif score == 6 or score == 7:
    print(congrats)
    print("\n-Nice! You did a good job!-")
elif score == 8 or score == 9:
    print(congrats)
    print("\n-You almost got the perfect score! You are too good for this!-")
else:
    print(congrats)
    print("\n-You nailed the game as just a piece of cake! You deserved to be in Harvard!-")
   

print(112 * "=")
os.system("pause")
os.system('cls')
print(112 * "=")
print("Thanks for playing this game! We hope you learned a lot and especially you've enjoyed it! See you next time!")
print(112 * "=")
print("...Closing the game in 5 seconds....")
print(112 * "=")
    
time.sleep(5)
os.system('cls')
sys.exit()