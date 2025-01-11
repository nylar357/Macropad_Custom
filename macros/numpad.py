# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x20660A, '7', ['7']),
        (0x20660A, '8', ['8']),
        (0x20660A, '9', ['9']),
        # 2nd row ----------
        (0x20660A, '4', ['4']),
        (0x20660A, '5', ['5']),
        (0x20660A, '6', ['6']),
        # 3rd row ----------
        (0x20660A, '1', ['1']),
        (0x20660A, '2', ['2']),
        (0x20660A, '3', ['3']),
        # 4th row ----------
        (0x660556, '*', ['*']),
        (0x800000, '0', ['0']),
        (0x660556, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
