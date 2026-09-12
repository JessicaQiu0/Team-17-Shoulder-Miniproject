# Software README

## Overview
This folder contains the MicroPython firmware for the meeting timer!

There are two main firmware files:

- `main.py` - standard meeting timer firmware
- `main_low_power.py` - meeting timer firmware with added low-power behavior (When the timer is not actively running, the ESP32 enters short 50 ms light sleep periods to reduce power use while still remaining responsive to button presses and LED updates)

The firmware controls:
- the stepper motor
- two push buttons
- three LEDs
- timer preset selection
- countdown behavior
- pause/resume behavior
- reset behavior

The timer supports four preset times:
- 15 minutes
- 20 minutes
- 25 minutes
- 30 minutes


## Pin Assignments

| Component | GPIO Pin |
|---|---:|
| Stepper Motor Coil 1 | GPIO 1 |
| Stepper Motor Coil 2 | GPIO 2 |
| Stepper Motor Coil 3 | GPIO 3 |
| Stepper Motor Coil 4 | GPIO 4 |
| Button 1 | GPIO 5 |
| Button 2 | GPIO 6 |
| Blue LED | GPIO 7 |
| Red LED | GPIO 8 |
| Green LED | GPIO 9 |


## Controls

### Button 1
Button 1 cycles through the preset timer values:

15 → 20 → 25 → 30 → 15

When a preset is selected, the stepper motor moves the clock hand to the corresponding position.


### Button 2
Button 2 controls the timer:

A short press:
- starts the timer
- pauses the timer while running
- resumes the timer while paused
- resets the timer after it finishes

Holding Button 2 for 2 seconds resets the timer and moves the hand back to 0.


## LED States
The LEDs indicate the current timer state:

- Blue: selecting a preset or paused
- Green: countdown running
- Red: countdown finished

The LEDs are controlled using PWM so the active LED pulses instead of remaining constantly on.


## Timer States

The firmware uses four states:

```python
SELECTING = 0
RUNNING = 1
PAUSED = 2
FINISHED = 3
