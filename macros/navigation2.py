from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Navigations', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xE95420, 'Apps', [Keycode.CONTROL, Keycode.SHIFT, 'A']),
        (0x024E9A, 'Launch',  [Keycode.CONTROL, Keycode.SPACE]),
        (0xE95420, 'Sublime',  [Keycode.CONTROL, Keycode.SHIFT, 'S']),
        # 2nd row ----------
        (0xFFE700, 'Dash', [Keycode.CONTROL, Keycode.SHIFT, 'O']),
        (0x024E9A, 'Files', [Keycode.CONTROL, 'f']),
        (0xFFE700, 'Fish', [Keycode.CONTROL, Keycode.SHIFT, 'K']),
        # 3rd row ----------
        (0xE95420, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x024E9A, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0xE95420, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 4th row ----------
        (0xA1D6CB, 'Wk L', [Keycode.CONTROL, ',']),
        (0x7E60BF, 'Min/Max', [Keycode.CONTROL, '/']),
        (0xA1D6CB, 'Wk R', [Keycode.CONTROL, '.']),  # Scroll up
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close Window
    ]
}
