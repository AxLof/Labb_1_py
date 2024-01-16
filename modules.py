import random

def divisible_integers(firstint, secondint):

    division_list = []

    for i in range(1, 1601):

        if i % firstint == 0 and i % secondint == 0:
            division_list.append(i)

    return division_list

def guessing_numbers():

    random_number = random.randint(1, 60)
    print('\nGuess a number between 1 and 60')
    input_number = int
    while input_number != random_number:

        try:
            input_number = int(input())

            if input_number == random_number:
                print(f'Correct, the number is {random_number}!')

            elif input_number > random_number:
                print('Too high, try again!')

            elif input_number < random_number:
                print('Too low, try again!')
        except ValueError:
            print('Wrong input type!')
            print('\nGuess a number between 1 and 60')
    return




