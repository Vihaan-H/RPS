import random

def accept_valid_input():
    player_rps_choice = None
    while True: 
        
        print('Please enter \n"rock" or "r" for rock\n"paper" or "p" for paper\n"scissors" or "s" for scissors ')
        player_rps_choice_unstripped = input() 
        player_rps_choice_uncapped = player_rps_choice_unstripped.strip()
        player_rps_choice = player_rps_choice_uncapped.lower()
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
def who_won(player_rps_choice,computer_choice):
    winning_decision = None
    if player_rps_choice == rock and computer_choice == paper:
        winning_decision = "Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!"
    elif player_rps_choice == scissors and computer_choice == rock:
        winning_decision = "Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!"
    elif player_rps_choice == paper and computer_choice == scissors:
        winning_decision = "Computer wins, AI WILL TAKE OVER THE WORLD ONE DAY!"
    elif player_rps_choice == scissors and computer_choice == paper:
        winning_decision = name + " won! Computer is sad 😭"
    elif player_rps_choice == paper and computer_choice == rock:
        winning_decision = name + " won! Computer is sad 😭"
    elif player_rps_choice == rock and computer_choice == scissors:
        winning_decision = name + " won! Computer is sad 😭"
    elif player_rps_choice == scissors and computer_choice == scissors:
        winning_decision = "It's a tie!"
    elif player_rps_choice == rock and computer_choice == rock:
        winning_decision = "It's a tie!"
    elif player_rps_choice == paper and computer_choice == paper:
        winning_decision = "It's a tie!"
    return winning_decision
def accept_player_name():
    while True:
        print("Please enter your first name: ")
        name = input().strip().title()
        if name == "" or '' or name == None:
            print("Oops. Your name cannot be blank. ")
        else:
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
winner = who_won(player_rps_choice,computer_decision)
print(winner)