# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'GameBar', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A3B66, '#1', ['1']),
        (0x663F00, '#2', ['2']),
        (0x0A3B66, '#3', ['3']),
        # 2nd row ----------
        (0x663F00, '#4', ['4']),
        (0x0A3B66, '#5', ['5']),
        (0x663F00, '#6', ['6']),
        # 3rd row ----------
        (0x0A3B66, '#7', ['7']),
        (0x202000, '#8', ['8']),
        (0x0A3B66, '#9', ['9']),
        # 4th row ----------
        (0x0A3B66, '*', ['*']),
        (0x800000, '0', ['0']),
        (0x0A3B66, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
