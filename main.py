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
    ans = '-'*len(random_word)
    while p.ret_lives():
        print(man(6-p.ret_lives()))
        print(f"Word : {ans}\t\tLives left : {p.ret_lives()}")
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
        if ans == random_word:
            print("Well done, you have won!!!")
            p.update_score(5)
            break
    if ans != random_word:
        print(
            f"\nSorry you coudn't guess the word which was : {random_word}\n")
    p.update_lives(6-p.ret_lives())


def rules():
    print("RULES".center(30, '='))


def hangman():
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
            print(f"\n{player.ret_name()}'s Score : {player.ret_score()}\n")
        elif inp == 3:
            rules()
        if val.upper() != 'Y':
            break


if __name__ == '__main__':
    hangman()
    pause("\nThank you for playing!!!\n\nPress any key to exit....")
