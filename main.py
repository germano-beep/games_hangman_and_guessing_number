def run_games():
    import forca
    import adivinhacao

    print('Chose the game you want to play')
    print('(1) Hangman (2) guessing game')
    game = int(input())

    if(game == 1):
        forca.play()
    elif(game == 2):
        adivinhacao.play()

if(__name__ == "__main__"):
    run_games()