'''Main file for the program'''
from getch import pause
from words import word
from body import man


class Player:
    '''
    Class to represent a player

    ...

    Attributes
    ----------
    lives : int
        lives left for the player
    name : str
        name of the player
    score : int
        score of the player

    Methods
    -------
    update_lives(num):
        Updates the current lives of the player by the given num.
    update_score(num):
        Updates the current score of the player by the given num.
    ret_lives():
        Returns the current lives of the player for displaying.
    ret_name():
        Returns the name of the player.
    ret_score():
        Returns the current score of the player for displaying.

    '''

    def __init__(self, pname) -> None:
        """
        Constructs all the necessary attributes for the Player object.
        Sets the current score , lives of the player to 0 , 6 respectively.

        Parameters
        ----------
            name : str
                first name of the person
        """
        self.lives = 6
        self.name = pname
        self.score = 0

    def update_lives(self, num):
        '''Updates the current lives of the player by the given num'''
        self.lives += num

    def update_score(self, num):
        '''Updates the current score of the player by the given num'''
        self.score += num

    def ret_lives(self):
        '''Returns the current lives of the player for displaying'''
        return self.lives

    def ret_name(self):
        '''Returns the name of the player'''
        return self.name

    def ret_score(self):
        '''Returns the current score of the player for displaying'''
        return self.score


def display_menu():
    '''Displays the menu to the player'''
    print(f"\n{'MENU'.center(30,'-')}")
    print("1    -->  Start Game")
    print("2    -->  Score")
    print("3    -->  Rules")
    print("Else -->  Exit")


def game(game_player):
    '''Function to handle the logic of the game'''
    random_word = word()
    ans = '-'*len(random_word)
    wrong_choice = ''
    while game_player.ret_lives():
        print(man(6-game_player.ret_lives()))
        print(f"Word : {ans}\t\tLives left : {game_player.ret_lives()}")
        print("Incorrect Guesses : ", wrong_choice)
        choice = input("Enter : ")
        if choice in random_word:
            # If the entered alphabet is in the word
            temp_word = ""
            for index, alphabet in enumerate(random_word):
                if alphabet == choice:
                    temp_word += choice
                elif ans[index] != '-':
                    temp_word += ans[index]
                else:
                    temp_word += '-'
            ans = temp_word
            game_player.update_score(1)
        else:
            # If the emtered alphabet is not in the word
            print("Your choice isn't present in the word, try again!!!")
            game_player.update_lives(-1)
            if not wrong_choice:
                wrong_choice += choice.upper()
            else:
                if choice.upper() in wrong_choice:
                    game_player.update_lives(1)
                    continue
                wrong_choice += " , " + choice.upper()
        if ans == random_word:
            # If the player correctly guessed the word
            print("Well done, you have won!!!")
            game_player.update_score(5)
            break
    if ans != random_word:
        # If the user exhausts all of the lives
        print(man(6))
        print(
            f"\nSorry you coudn't guess the word which was : {random_word}\n")
    game_player.update_lives(6-game_player.ret_lives())


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
            game(player)
            val = input("Do you want to play again? (Y/N) : ")
            if val.upper() == 'Y':
                game(player)
        elif inp == 2:
            print(f"\n{player.ret_name()}'s Score : {player.ret_score()}")
        elif inp == 3:
            rules()
        else:
            break
    pause(
        f"\nThank you for playing!!! Your total score: {player.ret_score()}\
            \n\nPress any key to exit....")


if __name__ == '__main__':
    hangman()
