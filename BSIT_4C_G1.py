import random

# FOR THE QUESTIONS AND CORRESPONDING ANSWERS
# Q4 MUST HAVE WHILE LOOP STATEMENT CORRECT TOO
# Q5 CAN BE ANSWERED AS CONTINUE
Questions = [
    ["What operator the difference of x and y: \n\t[A] /\n\t[B] %\n\t[C] //\n\t[D] -",
     "D"],
    ["What operator the true if x(left-hand argument) is less than y(right-hand argument): \n\t[A] <=\n\t[B] !=\n\t[C] <\n\t[D] >=",
     "C"],
    ["If a condition is true then logical not operator will make false: \n\t[A] NOT\n\t[B] AND\n\t[C] OR\n\t[D] IF",
     "A"],
    ["What operator to performs exponential(power) calculation on operators and assign value to the equivalent to left operand: \n\t[A] *=\n\t[B] %=\n\t[C] **=\n\t[D] //=",
     "C"],
    ["What is the meaning of '<<', '>>': \n\t[A] Comparisons, Identity, Membership operators\n\t[B] Bitwise Shift Operator\n\t[C] Unary plus, Unary minus, Bitwise NOT\n\t[D] Bitwise XOR",
     "B"],
    ["A statement consists of a boolean expression followed by one or more statements: \n\t[A] If Statement\n\t[B] Elif Statement\n\t[C] Else Statement\n\t[D] Single line If Statement",
     "A"],
    ["A statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 of a FALSE value: \n\t[A] If Statement\n\t[B] Elif Statement\n\t[C] Else Statement\n\t[D] Single line If Statement",
     "C"],
    ["Allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE: \n\t[A] If Statement\n\t[B] Elif Statement\n\t[C] Else Statement\n\t[D] Single line If Statement",
     "B"],
    ["If you have only one statement to execute, you can put it on the same line as the if statement: \n\t[A] If Statement\n\t[B] Elif Statement\n\t[C] Else Statement\n\t[D] Single line If Statement",
     "D"],
    ["If you have only one statement to execute, one for it, and one for else, you can put it all on the same line: \n\t[A] Single line If...Else Statement\n\t[B] Single line If Statement\n\t[C] Elif Statement\n\t[D] If Statement",
     "A"]
]

# RANDOMING --> SHUFFLE
random.shuffle(Questions)
# COUNT FOR THE CORRECT ANSWER
correctAnswers = 0
# COUNT FOR THE WRONG ANSWER
wrongAnswers = 0
# QUESTION NUMBERING
QuestionNumber = 1
# CHOICES
tries = 0
while tries <= 3:
    if tries == 3:
        print("Already answered 3 wrong answers")
        print("Exiting application....\n")
        exit(0)
    else:
        print("\nWELCOME TO QUIZ GAME")
        print("Do you want to play?")
        option = input("[Y]es \n[N]o \nEnter your answer: ")
        if option == 'y' or option == 'Y':
            name = input("Please enter your name: ")
            name = name.lower()
            name = name.capitalize()
            print("\nQUIZ GAME START!")
            # LOOPING
            # FROM 0 TO HOW MANY THE QUESTIONS IS, SKIP BY 1
            for i in range(0, len(Questions), 1):
                user_Answer = input("\n" + str(QuestionNumber) + ".) " +
                                    Questions[i][0] + "\nEnter you answer: ")
                if user_Answer.lower() == Questions[i][1].lower():
                    print("Correct Answer!")
                    correctAnswers += 1
                    QuestionNumber += 1
                else:
                    print("Wrong answer!")
                    print("The correct answer is "+Questions[i][1].upper())
                    wrongAnswers += 1
                    QuestionNumber += 1

            # DISPLAYING THE SCORES
            if correctAnswers > 5:
                print("")
                print("Job well done "+name+"! ")
            elif wrongAnswers > 5:
                print("")
                print("Nice try "+name+"! ")
            print("You got " + str(correctAnswers) + " right and " +
                  str(wrongAnswers) + " wrong answers")
            print("Thank you for answering the quiz\n")
            break
        elif option == 'n' or option == 'N':
            print("\nThank you for trying!")
            print("Have a nice day!\n")
            break
        else:
            print("Invalid input!\n")
            tries += 1
            continue
