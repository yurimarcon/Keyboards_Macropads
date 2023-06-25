
print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13
    )

keyboard.row_pins = (board.GP21, board.GP20, board.GP18, board.GP17, board.GP16)
#rollover_cols_every_rows = 4
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FN = KC.MO(1)
FN2 = KC.MO(2)
XXXXXXX = KC.TRNS

keyboard.keymap = [
    # Qwerty
    # ,-------------------------------------------------------------------------------------------------.
    # |XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|  ESC |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
    # |XXXXXX|XXXXXX|------+------+------+------+------+-------------+------+------+------+------+------|
    # |XXXXXX|XXXXXX| Tab  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |  '   |
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX| Shift|   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |   /  | Shift|
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX| Ctrl | GUI  |  Alt |  Fn2 |XXXXXX| Space| Space|  Alt |  Fn  |XXXXXX|XXXXXX| Enter|
    # `-------------------------------------------------------------------------------------------------'
    [
        XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,     KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BKSP, 
        XXXXXXX, XXXXXXX, KC.TAB,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,  
        XXXXXXX, XXXXXXX, KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,   
        XXXXXXX, XXXXXXX, KC.LCTRL, KC.LGUI, KC.LALT, FN2, XXXXXXX,     KC.SPC,  KC.SPC,  KC.RALT, FN,      XXXXXXX, XXXXXXX, KC.ENTER,  
    ],
    # Alt
    # ,-------------------------------------------------------------------------------------------------.
    # |XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|   '  |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |  ´   |
    # |XXXXXX|XXXXXX|------+------+------+------+------+-------------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      |      |      |      |      |      | Home | PgDn | PgUp | End  |   -  |   =  |
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      |  \|  | PIPE |      |      |      |      |      |      |      |      | Print|
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      |      |      |      |      |      |      |      |      |   [  |  ]   |      |
    # `-------------------------------------------------------------------------------------------------'

    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, KC.QUOT, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.LBRC,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.HOME, KC.PGDN, KC.PGUP, KC.END,  KC.MINS, KC.EQUAL,  
        XXXXXXX, XXXXXXX, XXXXXXX, KC.GRV,  KC.PIPE, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, KC.PSCR,  
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RBRC, KC.BSLS, XXXXXXX,  
    ],
    # Arrows
    # ,-------------------------------------------------------------------------------------------------.
    # |XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|XXXXXX|
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|  F1  |  F2  |  UP  |  F4  |  F5  |  F6  |  F7  |  F8  |  F9  | F10  | F12  | Del  |
    # |XXXXXX|XXXXXX|------+------+------+------+------+-------------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      | LEFT | DOWN | RIGHT|      |      | LEFT | DOWN |  UP  | RIGHT|      |      |
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      |      |      |      |      |      |      |      |      |      |      |      |
    # |XXXXXX|XXXXXX|------+------+------+------+------+------+------+------+------+------+------+------|
    # |XXXXXX|XXXXXX|      |      |      |      |      |      |      |      |      |      |      |      |
    # `-------------------------------------------------------------------------------------------------'

    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX, KC.F1,   KC.F2,   KC.UP,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,   KC.F12,   KC.DEL,
        XXXXXXX, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT,XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX
    ]
]

if __name__ == '__main__':
    keyboard.go()

