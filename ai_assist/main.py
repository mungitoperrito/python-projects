import pyperclip
import time

from pynput import keyboard
from pynput.keyboard import Key, Controller

# CONSTANTS
F8 = str(Key.f8.value)    # For exit
F9 = str(Key.f9.value)    # For fix line
F10 = str(Key.f10.value)  # For fix selection
SLEEP_DELAY = 0.3         # Allow for data transfer

def fix_current_line():
    pass


def fix_selection():

    # Step 1 - copy text to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')

    # Step 2 - get the text from the clipboard
    time.sleep(SLEEP_DELAY)
    text = pyperclip.paste()

    # Step 3 -

    # Step 4 - copy the text to the clipboard
    pyperclip.paste(text)

    # Step 5 - paste text into the doc
    with controller.pressed(Key.ctrl):
        controller.tap('v')


def on_f8():
    print('F8')
    exit()


def on_f9():
    print('F9')
    fix_current_line()


def on_f10():
    print('F10')
    fix_selection()



############
### MAIN ###
############

# Create keyboard control object
controller = Controller()

with keyboard.GlobalHotKeys({
        F8 : on_f8,
        F9 : on_f9,
        F10 : on_f10}) as hk:
    hk.join()
