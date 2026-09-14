# Project Overview

## Goal

Build a self-contained meeting timer with a mechanical display. The device lets a user select a preset duration, start/pause/reset the countdown, and see time remaining via a rotating clock hand while an RGB LED indicates the timer's current status. This project help our team to establish our GitHub workflow, collaborative process, and hardware-software development environment ahead of our Senior Design project.

## Description of Device

The meeting timer is built around a Seeed XIAO ESP32-S3 running MicroPython. A 28BYJ-48 stepper motor, driven through an L293D H-bridge, rotates a physical clock hand to show time remaining, moving from the selected preset position down to zero as the countdown progresses. An RGB LED communicates the current state through color and pulsing: blue for Selecting/Paused, green for Running, red for Finished. Two tactile buttons handle all user input. There is no screen, no wireless connection, and all of it is fully self-contained.

## Photo

![Meeting timer device](Mini%20project%20photo.jpeg)

## How to Use It

1. Power on the device via USB-C. The hand returns to the zero position.
2. Press **Button 1** to cycle through the four presets (15 / 20 / 25 / 30 minutes). The hand moves to reflect the selected duration.
3. Press **Button 2** to start the countdown. The hand begins moving toward zero and the LED switches to green.
4. Press **Button 2** again at any time to pause (LED returns to blue) or resume (LED returns to green).
5. Hold **Button 2** for 2 seconds at any point to reset the timer back to the selection state.
6. When the countdown reaches zero, the LED turns red and the hand returns to zero. Press **Button 2** to reset and select a new preset.

## Deliverables

- Working meeting timer with 15/20/25/30 minute presets
- Mechanical clock hand (stepper motor-driven) showing time remaining
- Two buttons for timer control (preset selection, start/pause/reset)
- RGB LED status indicator (PWM-pulsed)
- 3D-printed enclosure housing all components
- Full documentation: electrical schematic, firmware code, mechanical CAD, and a state chart/flowchart of system operation

## References

- Seeed Studio XIAO ESP32-S3 documentation
- MicroPython ESP32-S3 documentation
- L293D datasheet
- 28BYJ-48 stepper motor datasheet
