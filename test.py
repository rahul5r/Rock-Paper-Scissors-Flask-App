import random

def check_winner(user_choice, computer_choice):
    """
    rock vs paper -> paper wins
    rock vs scissors -> rock wins
    paper vs scissors -> scissors wins
    """
    if user_choice == computer_choice:
        return "Draw"
    # rock vs paper -> paper wins
    elif user_choice == 1 and computer_choice == 2:
        return "Computer"
    elif user_choice == 2 and computer_choice == 1:
        return "User"
    # rock vs scissors -> rock wins
    elif user_choice == 1 and computer_choice == 3:
        return "User"
    elif user_choice == 3 and computer_choice == 1:
        return "Computer"
    # paper vs scissors -> scissors wins
    elif user_choice == 2 and computer_choice == 3:
        return "Computer"
    elif user_choice == 3 and computer_choice == 2:
        return "User"


def get_choice(n):
    """
    1. Rock
    2. Paper
    3. Scissors
    """
    match n:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            return "Invalid"

def game():
    while True:
        print("Make your Choice (1-3)..")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = int(input("Enter Your choice :"))
        computer_choice = random.randint(1,3)
        print("User : ",get_choice(user_choice))
        print("Computer : ", get_choice(computer_choice))
        print("\nWinner : ", check_winner(user_choice,computer_choice))
        cont = int(input("Continue ?  (0 or 1) :"))
        if cont == 0:
            break

if __name__ == '__main__':
    game()

