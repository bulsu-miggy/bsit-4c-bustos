import random

questions = ["What is the description backslash notation '\\a'?",
"What is the description backslash notation '\\b'?",
"What is the description backslash notation '\\n'?",
"What is the description backslash notation '\\e'?",
"What is the description backslash notation '\\s'?",
"What symbol can combine two string values?",
"What symbol can duplicate strings?",
"What methods can changes all string letters to capitals?",
"What methods can converts all the string's letters into lower-case letters?",
"What methods can makes the first letter in each word upper-case?"
]
answers = ["A", "C", "D", "D", "C", "A", "D", "B", "B", "C"]
choices = ["A. Bell or Alert | C. Backspace \nB. Formfeed | D. Newline", 
"A. Bell or Alert | C. Backspace \nB. Formfeed | D. Newline",
"A. Bell or Alert | C. Backspace \nB. Formfeed | D. Newline",
"A. Space | C. Control-x \nB. tab | D. Escape",
"A. Vertical tab | C. Space \nB. tab | D. Escape",
"A. + | C. ! \nB. \ | D. *",
"A. + | C. ! \nB. \ | D. *",
"A. big() | C. upper() \nB. capitalize() | D. giant()",
"A. small() | C. low() \nB. lower() | D. mini()",
"A. small() | C. title() \nB. upper() | D. isuper()"
]
questionIndex = []
counter = 0
score = 0
answer = ""

while (counter <= len(questions) - 1):
#    print(counter)
    questionIndex.append(counter)
    counter += 1
questionIndex = random.sample(questionIndex, k=len(questionIndex))
#print(questionIndex)

counter = 1

print("Welcome!\nChoose the letter of the correct answer.")

for x in questionIndex:
    print("===============================================================")
    print(f'{"Question #"}{counter}{": "}{questions[x]}') 
    print(choices[x])       
    answer = input("Answer: ")
    if(answer.upper() == answers[x]):
        print("\nCorrect!")
        score += 1
    else:
        print("\nIncorrect")
    counter += 1       
print(f'{"Congratulations! Your score is: "}{score}')

