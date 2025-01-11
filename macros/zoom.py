
from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {  # REQUIRED dict, must be named 'app'
    "name": "Zoom",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # audio toggle
        (0x04541B, "Mic", [Keycode.CONTROL, Keycode.COMMAND, "a"]),
        (0x04541B, "", []),
        (0x04541B, "Camera", [Keycode.CONTROL, 0.1, Keycode.COMMAND, 0.1, "z"]),  # video toggle
        # 2nd row ----------
        (0x0A3B66, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x0A3B66, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x0A3B66, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 3rd row ----------
        # view toggle (gallery/speaker)
        (0x660556, "Speakr", [Keycode.SHIFT, Keycode.COMMAND, "="]),
        (0x800000, "Gallery", [Keycode.SHIFT, Keycode.COMMAND, "-"]),
        (0x660556, "Users", [Keycode.COMMAND, "k"]),  # participants toggle
        # 4th row ----------
        (0x800000, "FullScr", [Keycode.CONTROL, Keycode.COMMAND, "f"]),
        (0x660556, "Hand", [Keycode.ALT, "y"]),  # raise/lower hand
        (0x800000, "Chat", [Keycode.CONTROL, Keycode.COMMAND, "g"]),
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, Keycode.COMMAND, "q"]),  # close window
    ],
}