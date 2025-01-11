
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Navigation', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x4793AF, 'Wk L', [Keycode.CONTROL, ',']),
        (0x4793AF, 'Wk R', [Keycode.CONTROL, '.']),
        (0x4793AF, 'Swap Win', [Keycode.CONTROL, '/']),      # Scroll up
        # 2nd row ----------
        (0xDD5746, 'Apps', [Keycode.CONTROL, Keycode.SHIFT, 'A']),
        (0xDD5746, 'Launch',  [Keycode.CONTROL, Keycode.SPACE]),
        (0xDD5746, 'View',  [Keycode.CONTROL, Keycode.SHIFT, 'S']),
        # 3rd row ----------
        (0x00DFA2, 'Dash', [Keycode.CONTROL, Keycode.SHIFT, 'D']),
        (0x00DFA2, 'Files', [Keycode.CONTROL, 'f']),
        (0x00DFA2, 'Kitty', [Keycode.CONTROL, Keycode.SHIFT, 'K']),
        # 4th row ----------
        (0xFF0060, 'Vol+', [Keycode.F12]),
        (0xFF0060, 'Mute', [Keycode.F10]),
        (0xFF0060, 'Vol-', [Keycode.F11]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close Window
    ]
}
