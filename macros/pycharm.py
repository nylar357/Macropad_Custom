from consumer import Toolbar
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'PyCharm', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ---------
        (0x04541B, 'Find', 	[Keycode.CONTROL, Keycode.COMMAND, 'f']),
        (0x04541B, 'Replace', 	[Keycode.CONTROL, Keycode.COMMAND, 'r']),
        (0x04541B, 'Cut', 	[Keycode.CONTROL, Keycode.COMMAND, 'x']),
        # 2nd row ----------
        (0x0A3B66, 'Copy', 	[Keycode.CONTROL, Keycode.COMMAND, 'c']),
        (0x0A3B66, 'Paste', 	[Keycode.CONTROL, Keycode.COMMAND, 'v']),
        (0x0A3B66, 'Undo', 	[Keycode.CONTROL, Keycode.COMMAND, 'z']),
        # 3rd row ----------
        (0x660556, 'Save', 	[Keycode.CONTROL, Keycode.COMMAND, 's']),
        (0x800000, '+File', 	[Keycode.ALT, Keycode.COMMAND, 'Insert']),
        (0x660556, 'Settings', 	[Keycode.CONTROL, Keycode.ALT, Keycode.COMMAND, '']),
        # 4th row ----------
        (0x800000, 'Nautilus', 	[Keycode.CONTROL, Keycode.COMMAND, 'n']),
        (0x660556, 'Launch', 	[Keycode.CONTROL, Keycode.COMMAND 'space']),
        (0x800000, 'Exec', 	[Keycode.ALT, Keycode.COMMAND, 'space']),
        # Encoder button ---
        (0x000000, '', []) # Save for web
    ]
}
