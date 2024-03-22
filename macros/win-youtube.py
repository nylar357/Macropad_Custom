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
        (0x0A3B66, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x0A3B66, 'Mute', 'm'),
        (0x0A3B66, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x663F00, '<<10', 'j'),  # Rewind
        (0x663F00, 'Play', 'K'),  # Play/Pause
        (0x663F00, '10>>', 'l'),    # Fast Forward
        # 3rd row ----------
        (0x660556, 'Begin', '0'),  # Previous
        (0x660556, 'Caption', 'c'),
        (0x660556, 'Next', 'Shift+N'),    # Next
        # 4th row ----------
        (0x20660A, 'Mini', 'i'), # Cycle eyedropper/measure modes
        (0x20660A, 'Theater', 't'),   # Scale selection
        (0x20660A, 'Full', 'f'),    # Type tool
        # Encoder button ---
        (0x000000, '', []) # Save for web
    ]
}