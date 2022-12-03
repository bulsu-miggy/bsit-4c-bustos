import random

def QuizGame():
    Questionnaires = {
        "What type of Collection that are ordered and indexed?\n   [A] - Lists\n   [B] - Tuples\n   [C] - Dictionary\n   [D] - Sets" : "a",
        "What type of Collection that is the most powerful tool in Python?\n   [A] - Lists\n   [B] - Tuples\n   [C] - Dictionary\n   [D] - Sets" : "a",
        "Lists uses what kind of symbol to enclose its contents?\n   [A] - ( )\n   [B] - [ ]\n   [C] - { }\n   [D] - < >" : "b",
        "What type of Collection that is just like lists but immutable?\n   [A] - Lists\n   [B] - Tuples\n   [C] - Dictionary\n   [D] - Sets" : "b",
        "Tuples uses what kind of symbol to enclose its contents?\n   [A] - ( )\n   [B] - [ ]\n   [C] - { }\n   [D] - < >" : "a",
        "What type of Collection that are unordered, changeable, and indexed?\n   [A] - Lists\n   [B] - Tuples\n   [C] - Dictionary\n   [D] - Sets" : "c",
        "Dictionaries have _____ and _____?\n   [A] - Index and Element\n   [B] - Index and Values\n   [C] - Keys and Values\n   [D] - Row Index and Column Index" : "c",
        "Dictionaries uses what kind of symbol to enclose its contents?\n   [A] - ( )\n   [B] - [ ]\n   [C] - { }\n   [D] - < >" : "c",
        "What type of Collection that is an unordered and does not record element position or order of insertion?\n   [A] - Lists\n   [B] - Tuples\n   [C] - Dictionary\n   [D] - Sets" : "d",
        "Sets uses what kind of symbol to enclose its contents\n   [A] - ( )\n   [B] - [ ]\n   [C] - { }\n   [D] - < >" : "c" 
    }
    Questions = list(Questionnaires)
    random.shuffle(Questions)

    score = 0
    counter = 3
    QuestionNumber = 1
    while counter > 0:
        from itertools import islice
        FirstTenQuestions = islice(Questions,QuestionNumber-1,10)
        for key in FirstTenQuestions:
            print('\n'+ str(QuestionNumber)+ '.) ' + key)
            UserInput = input('\nEnter your answer: ')
            if UserInput.lower() == Questionnaires[key]:
                print('Correct!\n')
                score = score + 1
                QuestionNumber = QuestionNumber + 1
            elif UserInput.lower() != Questionnaires[key] and UserInput.lower() == 'a' or UserInput.lower() != Questionnaires[key] and UserInput.lower() == 'b' or UserInput.lower() != Questionnaires[key] and UserInput.lower() == 'c' or UserInput.lower() != Questionnaires[key] and UserInput.lower() == 'd':
                print('Incorrect\n')
                QuestionNumber = QuestionNumber + 1
            else:
                counter = counter - 1
                if counter > 0:
                    print('\nPlease enter the letter according to the choices!')
                    print(str(counter) + ' attempts remaining\n')
                break

        if QuestionNumber > 10:
            break
        elif counter == 0:
            print('\n\nYou have used your 3 attempts!')
            print('Your entry has been disqualified!')
            print('Thank you for playing the Quiz Game!\n')

    if counter != 0 and QuestionNumber > 10:
        QuestionNumber = QuestionNumber - 1
        print('\nYour score is ' + str(score) + '/'+ str(QuestionNumber) +'!\n\n')
        print('Do you want to play again?')
        UsersChoice()


def UsersChoice():
    i = 3
    while i > 0:
        i = i - 1
        condition = input('\nEnter your answer: ')
        if condition.lower() == 'y':
            print('\n\nHere are the questions:')
            QuizGame()
            break
        elif condition.lower() == 'n':
            print('\nThank you for visiting Quiz Game!\n')
            break
        elif i == 0:
            print('\n\nYou have used your 3 attempts!')
            print('Your entry has been disqualified!')
            print('Thank you for visiting the Quiz Game!\n')
        else:
            print('\nPlease choose Y or N!')
            print(str(i) + ' attempts remaining\n')


print('\nWelcome to Quiz Game!\n')
print('Do you want to play? Y|N')
UsersChoice()