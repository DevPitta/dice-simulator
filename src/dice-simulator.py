from random import randint

i = dices_sum = 0

while True:
    response = str(input('Would you like to play? [Y/N] ')).upper().strip()
    if response == 'Y':
        number_of_dices = int(input('How many dices would you like to roll? '))
        for i in range(number_of_dices):
            dice = randint(0, 6)
            i += 1
            dices_sum += dice
            print(f'Dice {i}: {dice}')
        print(f'You rolled {dices_sum} on the dices!')
    elif response == 'N':
        break
    else:
        print('Invalid answer! Please type Y or N')
