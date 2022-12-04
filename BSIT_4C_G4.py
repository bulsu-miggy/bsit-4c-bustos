import random

print("QUIZ GAME")
print("-------------------------")
name = input("Enter your name:")
choice = input("Hi " + name + " do you want to play the game? Y | N:")
print("-------------------------")
choice = choice.lower()
if choice != "y":
    quit()
score = 0                                   # starting score
check = []                                  # check if questions are not repeated during random
while len(check) != 10:
    questionNumber = random.randint(1, 10)

    if questionNumber == 1 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("A lot of functions that are installed together with Python.\nA. Pre-installed modules \nB.Lambda functions \nC.Filter function \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "a":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")
    
    if questionNumber == 2 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("It is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop.\nA. filler() \nB. map() \nC. diff() \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "b":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")
     
    if questionNumber == 3 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("It is small, anonymous functions. \nA. *args function \nB. Module function \nC. Lambda function \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "c":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")
    
    if questionNumber == 4 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("It is a built-in function that allows you to process an iterable and extract those items that satisfy a given condition. \nA. filter() \nB. *args() \nC.diff() \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "a":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n") 
               
    if questionNumber == 5 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input(" In User-Defined Functions, the line has to be ended with a __?: \nA. Semi Colon(;) \nB. Colon(:) \nC. Question mark(?) \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "b":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")  
                                        
    if questionNumber == 6 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input(" In User-Defined Functions, it always starts with the keyword __?: \nA. def \nB. deff \nC. define \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "a":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")          

    if questionNumber == 7 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input(" _ is a keyword argument that allows you to pass a variable number of non-keyword arguments to a Python function \nA. *kwargs \nB. *quack \nC. variable \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "c":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")  
            
    if questionNumber == 8 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input(" A ___ is a block of code that performs a specific task when it is called. \nA. loop \nB. function \nC. variable \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "b":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n") 
            
    if questionNumber == 9 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("Arguments are passed as Dictionary using __. The Dictionary will be accessible inside the function having the same name as the parameter without the asterisks(**). \nA. **kwargs \nB. *args \nC. filter() \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "a":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")                 
      
    if questionNumber == 10 and questionNumber not in check:
        check.append(questionNumber)
        questionAnswer = input("You can't define your own function using the def keyword.  \nA.True \nB.False \nC. None of the above \nYour answer:")
        questionAnswer = questionAnswer.lower()
        if questionAnswer == "b":
            score += 1
            print("Correct\n")
        else:
            print("Incorrect\n")       

percentage = int((score/10)*100)
percentage = str(percentage)
score = str(score)

print(name+ " you got " + score + " question(s) correct \nYour percentage is " + percentage +"%")
