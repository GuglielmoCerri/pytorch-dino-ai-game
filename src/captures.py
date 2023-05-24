import cv2
from PIL import ImageGrab
import numpy as np
import keyboard
import os
from datetime import datetime

current_key = ""
buffer = []

# check if folder named 'captures' exists. If not, create it.
if not os.path.exists("captures"):
    os.mkdir("captures")

def keyboardCallBack(key: keyboard.KeyboardEvent):
    '''
    This function is called when a keyboard event occurs. It stores the key pressed in a buffer and sorts it.

    ### Arguments : 
    `key (KeyboardEvent)`

    ### Returns : 
    `None`

    ### Example : 
    `keyboardCallBack(key)`
    '''

    global current_key

    if key.event_type == "down" and key.name not in buffer:
        buffer.append(key.name)

    if key.event_type == "up":
        buffer.remove(key.name)

    buffer.sort()  # Arrange the keys pressed in an ascending order
    current_key = " ".join(buffer)

keyboard.hook(callback=keyboardCallBack)
i = 0

while (not keyboard.is_pressed("esc")):

    # Capture image and save to the 'captures' folder with time and date along with the key being pressed
    image = cv2.cvtColor(np.array(ImageGrab.grab(
        bbox=(390, 220, 1000, 400))), cv2.COLOR_RGB2BGR)

    # if key pressed embed the key pressed in the file name
    if len(buffer) != 0:
        cv2.imwrite("captures/" + str(datetime.now()).replace("-", "_").replace(":",
                    "_").replace(" ", "_")+" " + current_key + ".png", image)

    # if no key pressed embed 'n' in the file name
    else:
        cv2.imwrite("captures/" + str(datetime.now()).replace("-",
                    "_").replace(":", "_").replace(" ", "_") + " n" + ".png", image)
    i = i+1