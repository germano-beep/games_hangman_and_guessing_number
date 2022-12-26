def play():
    import random
    print('********************')
    print('***guessing game!***')
    print('********************')

    number = round(random.randrange(1, 101))
    total_of_tryings = 0
    points = 1000

    print('Chose the level')
    print('(1) Easy (2) Medium (3) Hard')
    level = int(input())

    if(level == 1):
        total_of_tryings = 15
    elif(level == 2):
        total_of_tryings = 10
    else:
        total_of_tryings = 5

    for turn in range(1, total_of_tryings + 1):
        chosen_number = input('Write a number between 1 and 100:')
        chosen_number = int(chosen_number)
        print('Turn {} of {}'.format(turn, total_of_tryings))

        if(chosen_number < 1 or chosen_number > 100):
            print('You have to write a number between 1 and 100.')
            continue

        rightChosen = number == chosen_number
        bigger = number < chosen_number
        smaller = number > chosen_number

        if(rightChosen):
            print('You have chosen the right number. Your punctuation is {}'.format(points))
            break
        else:
            if (bigger):
                print('You have chosen the wrong number. The right is smaller!')
            elif (smaller):
                print('You have chosen the wrong number. The right is bigger!')

            lost_points = abs(number - chosen_number) * (4 - level)
            points -= lost_points

    print('The right number is {}!'.format(number))

if(__name__ == "__main__"):
    play()