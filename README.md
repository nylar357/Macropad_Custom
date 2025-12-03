# Macropad Custom Macros

A collection of custom macros for the **Adafruit Macropad RP2040**. I hope these will be helpful! They are designed to work on both **Linux & Windows**.

## 📺 Demo
Check out the macros in action:

[![Adafruit Macropad Custom Macros](https://img.youtube.com/vi/odwaIkPq_Fo/0.jpg)](https://www.youtube.com/watch?v=odwaIkPq_Fo)

## 🛠 Hardware Specifications: Adafruit Macropad RP2040
This project runs on the [Adafruit Macropad RP2040](https://www.adafruit.com/product/5128). If you are new to the board, here is what makes it tick:

* **Microcontroller:** Raspberry Pi RP2040 (Dual-core Cortex M0+ at ~130MHz)
* **Memory:** 264KB RAM + 8MB Flash storage (plenty of room for CircuitPython code)
* **Display:** 128x64 Monochrome OLED (SH1106) for crisp text and status updates
* **Inputs:**
    * 12x Mechanical Key Switches (Cherry MX compatible)
    * Rotary Encoder with Push-Button (20 detents per rotation)
* **Feedback:**
    * 12x RGB NeoPixels (one per key)
    * Class D Audio Amplifier with Speaker/Buzzer
* **Connectivity:** USB-C (Power/Data/MIDI/HID) & STEMMA QT Connector

---

## 🎵 Spotlight: Spotify Integration
### The Spotify bindings are designed for seamless context switching.
Script: rof.sh (Main Branch)
Function: Detects if Spotify is running.
If Running: Focuses the window immediately.
If Closed: Starts the application and then focuses it.

---

## 🚀 Installation & Setup

### 1. CircuitPython Files
There is no `code.py` editing needed from the default example. However, you must add the following helper files to your `CIRCUITPY` drive for some macros to function correctly:
* `consumer.py`
* `keyconfig.py`

### 2. Linux Dependencies (Spotify & Window Management)
To use the advanced **Spotify** and window focus features on Linux, you need to install a few utilities.

The `Spotify` macro uses `rof.sh` (located in the main branch) to check if Spotify is running. If it is, it focuses the window; if not, it launches it. This allows you to jump to your music regardless of your current workspace.

**Install dependencies via terminal:**
```bash
sudo apt-get install xprop wmctrl
```

Layer Description
Spotify NEW! Special bindings to focus/launch Spotify instantly.

Github Terminal commands for common GitHub workflows.

Linux-Firefox Shortcuts for Firefox (Works on Windows & Linux; Back/Forward buttons have Windows exception).

Media Standard media controls (Play/Pause, Vol +/-, Next/Prev).

Mouse Emulates mouse movement and clicks.
Navigation Desktop navigation shortcuts tailored for Arch Linux.

Navigations Desktop navigation shortcuts tailored for Ubuntu.

Numpad Standard Number Pad layout.
Tones Plays tones (same functionality as the default shipping example).

Twitter Shortcuts for navigating Twitter (X).

Vim Terminal command shortcuts for the Vim text editor.

Win-Youtube YouTube playback controls (specifically for Windows).

