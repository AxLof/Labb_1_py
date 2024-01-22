import modules


user_choice = 0

while user_choice != 3:
    try:
        print('\nMake a choice by entering a number between 1 and 3\n'
              '[1]: Divide two numbers\n'
              '[2]: Guess the number\n'
              '[3]: Exit program')
        user_choice = int(input())

        match user_choice:
            case 1:
                firstint = int(input('\nEnter first number: '))
                secondint = int(input('\nEnter second number: '))
                print('\n', modules.divisible_integers(firstint, secondint))
                continue

            case 2:
                modules.guessing_numbers()
                continue

            case 3:
                pass

            case default:
                print('\nPlease enter a valid number!')
    except ValueError:
        print('\nWrong input, please enter a number!')





