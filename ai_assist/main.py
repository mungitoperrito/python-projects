from pynput import keyboard
from pynput.keyboard import Key

# CONSTANTS
F8 = str(Key.f8.value)
F9 = str(Key.f9.value)
F10 = str(Key.f10.value)


def fix_current_line():
    pass


def fix_selection():
    pass


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

with keyboard.GlobalHotKeys({
        F8 : on_f8,
        F9 : on_f9,
        F10 : on_f10}) as hk:
    hk.join()
