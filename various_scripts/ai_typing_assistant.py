# Source
# Build a free writing assistant with Python and Ollama
# https://www.youtube.com/watch?v=IUTFrexghsQ


import httpx
import pyperclip
import time

from pynput import keyboard
from pynput.keyboard import Key, Controller
from string import Template

# CONSTANTS
F8 = str(Key.f8.value)    # For exit
F9 = str(Key.f9.value)    # For fix line
F10 = str(Key.f10.value)  # For fix selection
SLEEP_DELAY = 0.3         # Allow for data transfer

OLLAMA_GEN = "http://localhost:11434/api/generate"   # Local Ollama instance
OLLAMA_CONFIG = {"model": "mistral:instruct",
                 "keep_alive": "5m",
                 "stream": False
                 }
OLLAMA_HEADERS = {"Content-Type": "application/json"}

# NOTE: The "mistral:instruct" model is really slow.
#       The "mistral:7b-instruct-v0.2-q4_K_S" model is a lot faster

PROMPT_TEMPLATE = Template(
     """Fix all typos; fix all casing; fix all punctuation; and preserve
        any new line characters in this text:

        $text

        Return only the corrected text. Do not include a preamble.
    """
)

def fix_text(text):
    # Two 'text's: placeholder(from above) = argument(from function def)
    prompt = PROMPT_TEMPLATE.substitute(text=text)

    response = httpx.post(OLLAMA_GEN,
                json={"prompt": prompt, **OLLAMA_CONFIG},
                headers=OLLAMA_HEADERS,
                # Set to 10 in video. Ollama is very slow on my machine
                timeout=300
    )

    if response.status_code != 200:
        print(f"ERROR: returned {response.status_code}")

        return None

    # Note: Returns Ollama discussion for empty input line.
    #       Seems to hang, wihout timeout, on some inputs

    return response.json()['response'].strip()


def fix_current_line():
    # Select the current line <ctrl><i>
    controller.press(Key.ctrl)
    controller.press('i')
    controller.release(Key.ctrl)
    controller.release('i')

    # Call fix_selection to work on the selected line
    fix_selection()


def fix_selection():
    # Assumes there is alredy a selected chunk of text

    # Step 1 - copy text to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')

    # Step 2 - get the text from the clipboard
    time.sleep(SLEEP_DELAY)
    text = pyperclip.paste()

    # print(f"Copy: {text}")  # DEBUG

    # Step 3 - fix the text
    fixed_text = fix_text(text)

    # print(f"Fixed: {fixed_text}")  # DEBUG

    # Step 4 - copy the text to the clipboard
    pyperclip.copy(fixed_text)
    time.sleep(SLEEP_DELAY)

    # print(f"Paste: {fixed_text}")  # DEBUG

    # Step 5 - paste text into the doc
    with controller.pressed(Key.ctrl):
        controller.tap('v')


def on_f8():
    exit()


def on_f9():
    fix_current_line()


def on_f10():
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
