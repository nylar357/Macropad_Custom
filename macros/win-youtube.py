# SPDX-FileCopyrightText: 2022 DJDevon3 for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: YouTube Browser Controls
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'YouTube Player', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xF1E5D1, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x0A3B66, 'Mute', 'm'),
        (0x800000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0xB60071, '<<10', 'j'),  # Rewind
        (0xF1E5D1, 'Play', 'K'),  # Play/Pause
        (0x0A3B66, '10>>', 'l'),    # Fast Forward
        # 3rd row ----------
        (0xFF9A00, 'Begin', '0'),  # Previous
        (0xF1E5D1, 'Caption', 'c'),
        (0xFF9A00, 'Next', 'Shift+N'),    # Next
        # 4th row ----------
        (0x921A40, 'Mini', 'i'), # Cycle eyedropper/measure modes
        (0xDC84F3, 'Theater', 't'),   # Scale selection
        (0x921A40, 'Full', 'f'),    # Type tool
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}