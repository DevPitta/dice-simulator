import PySimpleGUI as sg

dice_1 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_1.png'
dice_2 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_2.png'
dice_3 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_3.png'
dice_4 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_4.png'
dice_5 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_5.png'
dice_6 = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_6.png'
dice_faces = '/media/pitta/Backup/Pitta/DEV/python-projects/beginner-projects/dice-simulator/images/dice_faces.png'


def dice_image(dice):
    if dice == 1:
        sg.popup(image=dice_1)
    if dice == 2:
        sg.popup(image=dice_2)
    if dice == 3:
        sg.popup(image=dice_3)
    if dice == 4:
        sg.popup(image=dice_4)
    if dice == 5:
        sg.popup(image=dice_5)
    if dice == 6:
        sg.popup(image=dice_6)
