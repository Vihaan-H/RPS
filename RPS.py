import random
print("This is a game of Rock, Paper, Scissors")
print("Please enter your name: ")
name = input()
#should be greeting based on time ↓
print(f"Hello, {name}! Let's play RPS.")


def accept_valid_input():
    while True: # 10 tries for now - change to forever
        rock = "rock"
        scissors = "scissors"
        paper = "paper"
        r = "r"
        s = "s"
        p = "p"
        print('Please enter \n"rock" or "r" for rock\n"paper" or "p" for paper\n"scissors" or "s" for scissors ')
        player_rps_choice = input()
        if player_rps_choice == rock: # bug no.1
            #↓ shouldnt say what user entered, should say scissors for s, etc
            print(f"You have chosen {player_rps_choice}")
            break
        elif player_rps_choice == paper:
                    #↓ shouldnt say what user entered, should say scissors for s, etc
                    print(f"You have chosen {player_rps_choice}")
                    break
        elif player_rps_choice == scissors:
                    #↓ shouldnt say what user entered, should say scissors for s, etc
                    print(f"You have chosen {player_rps_choice}")
                    break
        elif player_rps_choice == r: # bug no.1
                    player_rps_choice = rock
                    print(f"You have chosen {player_rps_choice}")
                    break
        elif player_rps_choice == p:
                            player_rps_choice = paper
                            print(f"You have chosen {player_rps_choice}")
                            break
        elif player_rps_choice == s:
                            player_rps_choice = scissors
                            print(f"You have chosen {player_rps_choice}")
                            break
         


def game_logic():
    accept_valid_input()
    choice = ["rock","paper","scissors"]
    computer_choice = random.choice(choice)
game_logic()
