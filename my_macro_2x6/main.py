# SPDX-FileCopyrightText: 2021 Pierre Constantineau
# SPDX-License-Identifier: MIT
# Raspberry Pi Pico 4x4 Macropad 
"""
    Code adapted from the following sources:
    MACROPAD Hotkey (https://learn.adafruit.com/macropad-hotkeys/project-code)
    Pico Four Keypad  (https://learn.adafruit.com/pico-four-key-macropad/code-the-four-keypad)
"""
import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

#==========================================================
    # MOUSE CONFIGURATION
from adafruit_hid.mouse import Mouse
import digitalio
import time

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False
#==========================================================

kpd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kpd)

# define keys for 4x4 v2
keys = keypad.Keys(
    pins=(
        board.GP16, board.GP17, board.GP18,
        board.GP19,board.GP20, board.GP21,
        #========== PINOS NÃO UTILIZADOS ========================
        board.GP3, board.GP4,board.GP5, board.GP6,
        board.GP7, board.GP8,board.GP9, board.GP10,
        board.GP15, board.GP22
        #=========================================================
    ),
    value_when_pressed=False
)

keymap = [
    ("pull", ['git pull']),
    ("fetch", ['git fetch']),
    ("add", ['git add .']),
    ("status", ['git status']),
    ("commit", ['git commit -m']),
    ("push", ['git push']),
    #============= COMANDOS NÃO UTILIZADOS ===========
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V]),
    ("Select all", [Keycode.LEFT_CONTROL, Keycode.A]),
    ("Cut1", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V]),
    ("Select all", [Keycode.LEFT_CONTROL, Keycode.A]),
    ("Cut2", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V])
]

print("keymap:")
for key in keymap:
    print("\t", key[0])

while True:
    key_event = keys.events.get()
    
    if key_event:
        led.value = True
        
        if key_event.pressed:
            print(keymap[key_event.key_number])
            
            sequence = keymap[key_event.key_number][1]
            
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        print("=> ",item)
                        kpd.press(item)
                    else:
                        kpd.release(-item)
                else:
                    keyboard_layout.write(item)        
        else:
            # Release any still-pressed modifier keys
            sequence = keymap[key_event.key_number][1]
            for item in sequence:
                if isinstance(item, int) and item >= 0:
                    kpd.release(item)
        
        led.value = False
