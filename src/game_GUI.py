import PySimpleGUI as sg
from random import randint
from dice_images import dice_image, dice_faces


class Game:
    def roll_dices(self):
        """Roll the dices"""
        i = dices_sum = dices = 0
        while True:
            dices = self.values['dice']
            if not dices.isdigit():
                sg.popup('Type only numbers', text_color='red')
                print("Error! Type only numbers.")
                break
            else:
                dices = int(dices)
                for i in range(dices):
                    dice = randint(1, 6)
                    dice_image(dice)
                    i += 1
                    dices_sum += dice
                    if dices != 1:
                        print(f'Dice {i}: {dice}')
                if dices == 1:
                    print(f'You rolled {dice} on the dice')
                elif dices == 0:
                    print('You must have to roll at least one dice!')
                else:
                    print(f'You rolled {dices_sum} on the dices!')
            break


class PythonScreen(Game):
    def __init__(self):
        # Change color layout
        sg.change_look_and_feel('Dark Blue 3')
        # Layout
        layout = [
            [sg.Image(filename=dice_faces)],
            [sg.Text('Name', tooltip='Enter your first name', size=(7, 0)), sg.Input(size=(15, 0), key='name')],
            [sg.Text('Dice(s)', tooltip='Enter the number of dices', size=(7, 0)), sg.Input(size=(15, 0), key='dice')],
            [sg.Button("Roll dice(s)", tooltip='Roll dice(s)')],
            [sg.Output(size=(30, 20))]
        ]
        # Window
        self.window = sg.Window("Dice Simulator").layout(layout)

    def Start(self):
        while True:
            # Extract screen data
            self.button, self.values = self.window.Read()
            name = self.values['name']
            print(f'Welcome to the Dice Simulator {name}!')
            self.roll_dices()
            if sg.popup_yes_no('Do you want to roll dice(s) again?') == 'No':
                sg.popup_ok('END GAME', text_color='red')
                break
            print('-' * 30)
