import random
import time

def main():
    GameList = ["Snake", "Water", "Gun"]
    round = 10
    player_point = 0
    computer_point = 0
    print("Welcome\nYou have total 10 rounds")
    while round:
        time.sleep(2)
        print()
        print("Turn :-",11 - round)
        print("1. Snake\n2. Water\n3. Gun")
        choice = int(input("Enter your choice : "))
        computer = random.choice(GameList)
        print()
        if(computer == "Snake" and choice == 1):
            print("Draw\nComputer : Snake\nPlayer : Snake")
            player_point += 1
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Snake" and choice == 2):
            print("Computer Won this round\nComputer : Snake\nPlayer : Water")
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Snake" and choice == 3):
            print("Player won this round\nComputer : Snake\nPlayer : Snake")
            player_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Water" and choice == 1):
            print("Player Won\nComputer : Water\nPlayer : Snake")
            player_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Water" and choice == 2):
            print("Draw\nComputer : Water\nPlayer : Water")
            player_point += 1
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Water" and choice == 3):
            print("Computer Won\nComputer : Water\nPlayer : Gun")
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Gun" and choice == 1):
            print("Computer Won\nComputer : Gun\nPlayer : Snake")
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Gun" and choice == 2):
            print("Player Won\nComputer : Gun\nPlayer : Water")
            player_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif(computer == "Gun" and choice == 3):
            print("Draw\nComputer : Gun\nPlayer : Gun")
            player_point += 1
            computer_point += 1
            round -= 1
            print(f"Player = {player_point} and Computer = {computer_point}")
    else :
        time.sleep(2)
        print()
        if computer_point > player_point:
            print("Computer Won the Game")
            print(f"Player = {player_point} and Computer = {computer_point}")
        elif computer_point < player_point:
            print("Player Won the Game")
            print(f"Player = {player_point} and Computer = {computer_point}")
        else :
            print("Its Draw")
            print(f"Player = {player_point} and Computer = {computer_point}")

    if input("Do You Want To Play Again : (Y/N) :") in ('Y','y'):
        main()
    else :
        print("Thank U")
        exit(0)

main()