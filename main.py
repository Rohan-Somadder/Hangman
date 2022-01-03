from words import word
from body import man
from getch import pause


class Player:
    def __init__(self, pname) -> None:
        self.lives = 6
        self.name = pname
        self.score = 0

    def update_lives(self, num):
        self.lives += num

    def update_score(self, num):
        self.score += num

    def ret_lives(self):
        return self.lives

    def ret_name(self):
        return self.name

    def ret_score(self):
        return self.score


def display_menu():
    print("MENU".center(30, "-"))
    print("1    -->  Start Game")
    print("2    -->  Score")
    print("3    -->  Rules")
    print("Else -->  Exit")


def game(p):
    random_word = word()
    w_set = set(random_word)
    while p.ret_lives():
        ans = '-'*len(random_word)
        print(f"Word : {ans}")
        s = input("Enter : ")
        if s in w_set:
            pass
        else:
            print("Your choice isn't present in the word, try again!!!")
            p.update_lives(-1)


def rules():
    print("RULES".center(30, '='))


def hangman():
    name = input("Enter Your Name: ")
    player = Player(name)
    while True:
        val = 'N'
        display_menu()
        try:
            inp = int(input("Enter your choice: "))
        except ValueError:
            inp = -1
        if inp == 1:
            game(player)
            val = input("Do you want to play again? (Y/N) : ")
        elif inp == 2:
            print(f"\n{player.ret_name()}'s Score : {player.ret_score()}\n")
            val = 'Y'
        elif inp == 3:
            rules()
            val = 'Y'
        if val.upper() != 'Y':
            break


if __name__ == '__main__':
    hangman()
    pause("\n\nThank you for playing!!! \n\nPress any key to exit....")
