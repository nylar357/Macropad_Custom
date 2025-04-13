from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Spotify', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0060, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0xFF76CE, 'Spotify',  [Keycode.CONTROL, Keycode.ALT, 's']),
        (0xFF0060, 'Vol+',  [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0xFF9A00, '<<10', [[ConsumerControlCode.REWIND]]),
        (0xFF76CE, 'Play', [Keycode.SPACE]),
        (0xFF9A00, '45>>', [[ConsumerControlCode.FAST_FORWARD]]),
        # 3rd row ----------
        (0xDD5746, 'Lib', [Keycode.SHIFT, Keycode.ALT, 'l']),
        (0xFF76CE, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0xDD5746, 'Info', [Keycode.SHIFT, Keycode.ALT, 'r']),
        # 4th row ----------
        (0x024E9A, 'Liked', [Keycode.SHIFT, Keycode.ALT, 's']),
        (0x660556, '4 U', [Keycode.SHIFT, Keycode.ALT, 'm']),
        (0x024E9A, 'Charts', [Keycode.SHIFT, Keycode.ALT, 'c']),  # Scroll up
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close Window
    ]
}
