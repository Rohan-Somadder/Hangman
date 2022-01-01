from words import word
from body import man


class player:
    def __init__(self, pname) -> None:
        self.lives = 6
        self.name = pname

    def update_lives(self, num):
        self.lives += num

    def ret_lives(self):
        return self.lives


def display_menu():
    print("MENU".center(30, "-"))
    print("1    -->  Start Game")
    print("2    -->  Score")
    print("3    -->  Rules")
    print("Else -->  Exit")


def hangman():
    name = input("Enter Your Name: ")
    pl = player(name)
    display_menu()
    try:
        inp = int(input("Enter your choice: "))
    except:
        inp = -1
    if inp == 1:
        pass
    elif inp == 2:
        pass
    elif inp == 3:
        pass


if __name__ == '__main__':
    hangman()
