from random import randint
from time import sleep
from colors import FontColors, Styles

color = FontColors()
style = Styles()


class Game:
    def __init__(self):
        pass

    def play_game(self):
        header()
        sleep(1)
        player = str(input('Which is your name? '))
        print(f'{color.green}Welcome to the Dice Simulator {player}!{style.end}')
        sleep(0.5)
        response = str(input('Would you like to play? [Y/N] ')).upper().strip()
        sleep(0.5)
        while True:
            if response == 'Y':
                self.roll_dices()
                response = str(input('Would you like to play again? [Y/N] ')).upper().strip()
            elif response == 'N':
                break
            else:
                response = str(input('Invalid answer! Please type Y or N: ')).upper().strip()
        print(f'{color.cyan}Thanks for playing {player}. Check back often!{style.end}')

    def roll_dices(self):
        """Roll the dices"""
        i = dices_sum = dices = 0
        while True:
            dices = input('How many dices would you like to roll? ')
            if not dices.isdigit():
                print(f'{color.red}Type only numbers!{style.end}')
            else:
                dices = int(dices)
                break
        for i in range(dices):
            dice = randint(1, 6 + 1)
            i += 1
            dices_sum += dice
            if dices != 1:
                print(f'Dice {i}: {dice}')
                sleep(1)
        if dices == 1:
            sleep(1)
            print(f'{color.yellow}You rolled {dice} on the dice{style.end}')
        elif dices == 0:
            print(f'{color.red}You must have to roll at least one dice!{style.end}')
        else:
            print(f'{color.yellow}You rolled {dices_sum} on the dices!{style.end}')


def header():
    title = 'DICE SIMULATOR'
    title_length = len(title)
    print('-' * title_length)
    print(f'{style.bold}{title}{style.end}')
    print('-' * title_length)
