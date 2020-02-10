from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = (200,100)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type('I am freaking awesome!')

controlKeyboard()
# controlling your mouse
# listening to your mouse
# controlling your keyword
# listening to your keyboard - will be finally used in keylogger