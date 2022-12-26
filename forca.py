import random

def play():
    welcome_message()
    word = choose_secret_word()

    list_chosen_letters = ['_' for letter in word]

    right_word = False
    tryings = 0

    while(not right_word):
        chosen_letter = choose_letter_function()
        if (chosen_letter in word):
            list_chosen_letters = save_corrects_chosen_letters(chosen_letter, word, list_chosen_letters)
            right_word = is_the_right_word(list_chosen_letters)
            if(right_word):
                print(list_chosen_letters)
                break
        else:
            tryings += 1
            if(tryings == len(word)):
                break
        print(list_chosen_letters)
        print("You got {} tryings!".format(len(word) - tryings))

    game_over_message(word, right_word)

def choose_letter_function():
    letter_choice = input("Chose a letter: ")
    letter_choice = letter_choice.strip().upper()
    return letter_choice

def welcome_message():
    print('********************')
    print('******Hangman!******')
    print('********************')

def choose_secret_word():
    words = []
    file = open('palavras.txt', 'r')

    for word_file in file:
        words.append(word_file.strip())

    number = random.randrange(0, len(words))

    word = words[number].upper()
    print(word)
    return word

def save_corrects_chosen_letters(letter, w, list_letters):
    index = 0
    for let in w:
        if (let == letter):
            list_letters[index] = let
        index += 1
    return list_letters

def is_the_right_word(list):
    if ("_" not in list):
        return True

def game_over_message(w, right_w):
    if (right_w):
        print("Congratulations!!! You chose the correct word: {}".format(w))
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("I'm sorry, the correct word was {}".format(w))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

if(__name__ == '__main__'):
    play()