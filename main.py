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
    print(f"\n{'MENU'.center(30,'-')}")
    print("1    -->  Start Game")
    print("2    -->  Score")
    print("3    -->  Rules")
    print("Else -->  Exit")


def game(p):
    random_word = word()
    ans = '-'*len(random_word)
    wrong_choice = ''
    while p.ret_lives():
        print(man(6-p.ret_lives()))
        print(f"Word : {ans}\t\tLives left : {p.ret_lives()}")
        print("Incorrect Guesses : ", wrong_choice)
        ch = input("Enter : ")
        if ch in random_word:
            temp_word = ""
            for i, s in enumerate(random_word):
                if s == ch:
                    temp_word += ch
                elif ans[i] != '-':
                    temp_word += ans[i]
                else:
                    temp_word += '-'
            ans = temp_word
            p.update_score(1)
        else:
            print("Your choice isn't present in the word, try again!!!")
            p.update_lives(-1)
            if not wrong_choice:
                wrong_choice += ch.upper()
            else:
                wrong_choice += " , " + ch.upper()
        if ans == random_word:
            print("Well done, you have won!!!")
            p.update_score(5)
            break
    if ans != random_word:
        print(man(6))
        print(
            f"\nSorry you coudn't guess the word which was : {random_word}\n")
    p.update_lives(6-p.ret_lives())


def rules():
    print(f"\n{'RULES'.center(30, '=')}")
    print("1. A random word is choosen try to guess it by guessing its letters.")
    print("2. You have 6 lives.")
    print("3. For each correct letter you get 1 point.")
    print("4. And if you get the word correct you get 5 more points.")
    print("\nHave fun playing and guessing...")


def hangman():
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
        elif inp == 2:
            print(f"\n{player.ret_name()}'s Score : {player.ret_score()}")
        elif inp == 3:
            rules()
        if val.upper() != 'Y':
            break
    pause(
        f"\nThank you for playing!!! Your total score: {player.ret_score()}\n\nPress any key to exit....")


if __name__ == '__main__':
    hangman()
