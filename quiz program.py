def ask():
    quiz = {
        "question1" : {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        "question2" : {
            "question": "What is the capital of Germany?",
            "answer": "Berlin"
        },
        "question3" : {
            "question": "What is the capital of Italy?",
            "answer": "Roma"
        },
        "question4" : {
            "question": "What is the capital of Spain?",
            "answer": "Madrid"
        },
        "question5" : {
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon"
        },
        "question6" : {
            "question": "What is the capital of Switzerland?",
            "answer": "Bern"
        },
        "question7" : {
            "question": "What is the capital of Austria?",
            "answer": "Vienna"
        },
    
    }

    score = 0

    for key, value in quiz.items():
        print(value['question'])
        answer = input("Answer? ")
    
        if answer.lower() == value['answer'].lower():
            print('Correct')
            score =  score + 1
            print("Your Score: " + str(score))
            print("")
            print("")
        else:
            print("Wrong!")
            print("The Answer is : " + value['answer'])
            print("Your Score is : " + str(score))
            print("")
            print("")

    print("You got " + str(score) + " out of 7 question correctly")
    print("Your percentage is " + str(int(score/7 * 100)) + " %")


    while True:
        replay = input("Still Wanna Play ? (y/n) ")
        if replay == "Y" or replay == "y":
            ask()
        else:
            quit()

print("Welcome to Our Quiz!!")
ask()
