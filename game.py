'''File containing the game logic'''


# Importing the required functions
from words import word
from body import man


def game(player):
    '''Function to handle the logic of the game'''

    random_word = word()
    user_input = '-'*len(random_word)
    wrong_choice = ''

    while player.ret_lives():
        print(man(6-player.ret_lives()))
        print(f"Word : {user_input}\t\tLives left : {player.ret_lives()}")
        print("Incorrect Guesses : ", wrong_choice)
        choice = input("Enter : ")

        if choice in random_word:
            # If the entered alphabet is in the word
            temp_word = ""
            for index, alphabet in enumerate(random_word):
                if alphabet == choice:
                    temp_word += choice
                elif user_input[index] != '-':
                    temp_word += user_input[index]
                else:
                    temp_word += '-'
            user_input = temp_word
            player.update_score(1)
        else:
            # If the emtered alphabet is not in the word
            print("Your choice isn't present in the word, try again!!!")
            player.update_lives(-1)
            if not wrong_choice:
                wrong_choice += choice.upper()
            else:
                if choice.upper() in wrong_choice:
                    player.update_lives(1)
                    continue
                wrong_choice += " , " + choice.upper()
        if user_input == random_word:
            # If the player correctly guessed the word
            print("Well done, you have won!!!")
            player.update_score(5)
            break
    if user_input != random_word:
        # If the user exhausts all of the lives
        print(man(6))
        print(
            f"\nSorry you coudn't guess the word which was : {random_word}\n")
    # Updates player lives back to 6 after a game
    player.update_lives(6-player.ret_lives())
