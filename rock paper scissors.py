import random

def main():
    exit = False
    user_points = 0
    computer_point = 0
    
    while exit == False:
        options = ["rock", "paper", "scissors"]
        user_input = input("Choose rock, paper, scissors or exit ")
        computer_input = random.choice(options)
        
        if user_input == "exit":
            print("Game Ended")
            #Made declaration of status
            if user_points < computer_point:
                word_for_you = 'You Lose'
                print(word_for_you+ " ,You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_point))
            elif user_points > computer_point:
                word_for_you = 'You Won'
                print(word_for_you+ " ,You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_point))
            elif user_points == computer_point:
                word_for_you = 'Its A Tie'
                print(word_for_you+ " ,You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_point))
            
            exit = True
            #Choice to play again after input exit word
            input_again = input("Still Wanna Play Again?(y/n) ")  
            if input_again == 'Y' or input_again == 'y':
                main()
            elif input_again == 'N' or input_again == 'n':
                print("Goodbye, Come Again")
                quit()

        if user_input == "rock" :
            if computer_input == "rock":
                print("Your input is rock")
                print("Computer input is rock")
                print("Draw")
            elif computer_input == "paper":
                print("Your input is rock")
                print("Computer input is paper")
                print("You Lose")
                computer_point += 1
            elif computer_input == "scissors":
                print("Your input is rock")
                print("Computer input is scissors")
                print("You Won")
                user_points += 1
        elif user_input == "paper":
            if computer_input == "rock":
                print("Your input is paper")
                print("Computer input is rock")
                print("You Won")
                user_points += 1
            elif computer_input == "paper":
                print("Your input is paper")
                print("Computer input is paper")
                print("Draw")
            elif computer_input == "scissors":
                print("Your input is paper")
                print("Computer input is scissors")
                print("You Lose") 
                computer_point += 1
        elif user_input == "scissors":
            if computer_input == "rock":
                print("Your input is scissors")
                print("Computer input is rock")
                print("You Lose")
                computer_point += 1
            elif computer_input == "paper":
                print("Your input is scissors")
                print("Computer input is paper")
                print("You Won")
                user_points += 1
            elif computer_input == "scissors":
                print("Your input is scissors")
                print("Computer input is scissors")
                print("Draw")   
        elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
            print("Invalid Input, Not Count")
            #When you input wrong option, its still give you score and not count for your score
            print("You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_point))
               

main()

