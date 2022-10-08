'''Main file for the program'''
from getch import pause
from game import game
from player import Player

def display_menu():
    '''Displays the menu to the player'''
    print(f"\n{'MENU'.center(30,'-')}")
    print("1    -->  Start Game")
    print("2    -->  Score")
    print("3    -->  Rules")
    print("Else -->  Exit")


def rules():
    '''Displays the rules to the player when the player wants to see'''
    print(f"\n{'RULES'.center(30, '=')}")
    print("1. A random word is choosen try to guess it by guessing its letters.")
    print("2. You have 6 lives.")
    print("3. For each correct letter you get 1 point.")
    print("4. And if you get the word correct you get 5 more points.")
    print("\nHave fun playing and guessing...")


def hangman():
    '''Main function to control the different functions'''
    print(f"\n{'HANGMAN'.center(30,'~')}\n")
    name = input("Enter Your Name: ")
    player = Player(name)
    while True:
        display_menu()
        try:
            inp = int(input("Enter your choice: "))
        except ValueError:
            inp = -1
        val = 'Y' if 0 < inp <= 3 else 'N'
        if inp == 1:
            while val.upper() == 'Y':
                game(player)
                val = input("Do you want to play again? (Y/N) : ")
                # if val.upper() == 'Y':
                #     game(player)
        elif inp == 2:
            print(f"\n{player.ret_name()}'s Score : {player.ret_score()}")
        elif inp == 3:
            rules()
        else:
            break
    pause(
        f"\nThank you for playing {player.ret_name()}!!! Your total score: {player.ret_score()}\
            \n\nPress any key to exit....")


if __name__ == '__main__':
    hangman()
