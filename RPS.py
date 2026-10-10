import random


def accept_valid_input():
    player_rps_choice = None
    while True: 
        
        print('Please enter \n"rock" or "r" for rock\n"paper" or "p" for paper\n"scissors" or "s" for scissors ')
        player_rps_choice_unstripped = input() 
        player_rps_choice = player_rps_choice_unstripped.strip()
        if player_rps_choice == rock: 
            
            print(f"You have chosen {player_rps_choice}")
            return player_rps_choice
        elif player_rps_choice == paper:
                    
                    print(f"You have chosen {player_rps_choice}")
                    return player_rps_choice
        elif player_rps_choice == scissors:
                    
                    print(f"You have chosen {player_rps_choice}")
                    return player_rps_choice
        elif player_rps_choice == r: # bug no.1
                    player_rps_choice = rock
                    print(f"You have chosen {player_rps_choice}")
                    return player_rps_choice
        elif player_rps_choice == p:
                            player_rps_choice = paper
                            print(f"You have chosen {player_rps_choice}")
                            return player_rps_choice
        elif player_rps_choice == s:
                            player_rps_choice = scissors
                            print(f"You have chosen {player_rps_choice}")
                            return player_rps_choice
def random_computer_decision():
    choice = ["rock","paper","scissors"]
    computer_choice = random.choice(choice)
    print (f"The computer chose {computer_choice}")
    return computer_choice
def who_won(computer_choice):
    if player_rps_choice == rock and computer_choice == paper:
        print("Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!")
    elif player_rps_choice == scissors and computer_choice == rock:
        print("Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!")
    elif player_rps_choice == paper and computer_choice == scissors:
        print("Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!")
    elif player_rps_choice == scissors and computer_choice == paper:
        print(f"{name} won! Computer is sad 😭")
    elif player_rps_choice == paper and computer_choice == rock:
        print(f"{name} won! Computer is sad 😭")
    elif player_rps_choice == rock and computer_choice == scissors:
        print(f"{name} won! Computer is sad 😭") 
    elif player_rps_choice == scissors and computer_choice == scissors:
        print("It's a tie!")
    elif player_rps_choice == rock and computer_choice == rock:
        print("It's a tie!")
    elif player_rps_choice == paper and computer_choice == paper:
        print("It's a tie!")
def accept_player_name():
    while True:
        print("Please enter your name: ")
        name_unstripped = input()
        name = name_unstripped.strip()
        if name == "" or name == None:
            print("Please enter your name: ")
            name = input()
        else:
            break
    return name
computer_choice = None
rock = "rock"
scissors = "scissors"
paper = "paper"
r = "r"
s = "s"
p = "p"

#calling section ↓
print("This is a game of Rock, Paper, Scissors")
name = accept_player_name()
#should be greeting based on time ↓
print(f"Hello, {name}! Let's play RPS.")
player_rps_choice = accept_valid_input() 
computer_decision = random_computer_decision()
who_won(computer_decision)