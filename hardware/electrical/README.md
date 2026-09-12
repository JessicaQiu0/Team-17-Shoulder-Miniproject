# Electrical

## Contents

| File | Description |
|------|-------------|
| `Electrical_Schematic.pdf` | Full circuit schematic |
| `Electrical_Schematic.kicad_sch` | Editable KiCad source file |

## Overview

This circuit implements a timer with a mechanical countdown display. A user selects a preset time (15/20/25/30 min) and starts the timer using two buttons. As time counts down, a stepper motor rotates a clock hand to show time remaining, while an RGB LED pulses to indicate the timer's status (e.g., running, paused, or finished).

**Motor control:** Since the XIAO's GPIO pins output 3.3V and can't directly drive the motor, an L293D H-bridge driver sits between them. It takes the 3.3V logic signals and switches the motor's 5V power accordingly. The stepper is driven using wave-pulse sequencing (energizing one coil at a time in sequence) to rotate the clock hand.

**LED feedback:** A common-cathode RGB LED, current-limited with 220Ω resistors on each color leg, is PWM-driven by the microcontroller to pulse and change color based on timer state.

**User input:** Two push buttons let the user select a preset and control start/pause/reset, read directly by the microcontroller's GPIO pins.

## Pin Mapping

### XIAO ESP32-S3 → L293D (motor control)

| XIAO Pin | L293D Pin | Function |
|----------|-----------|----------|
| GPIO1 | Pin 2 (1A) | Motor coil 1 signal |
| GPIO2 | Pin 7 (2A) | Motor coil 2 signal |
| GPIO3 | Pin 10 (3A) | Motor coil 3 signal |
| GPIO4 | Pin 15 (4A) | Motor coil 4 signal |

### L293D → Motor (28BYJ-48)

| L293D Pin | Motor Wire |
|-----------|------------|
| Pin 3 (1Y) | Orange (Coil 1) |
| Pin 6 (2Y) | Pink (Coil 2) |
| Pin 11 (3Y) | Yellow (Coil 3) |
| Pin 14 (4Y) | Blue (Coil 4) |
| — | Red (+5V, direct to 5V rail) |

### XIAO ESP32-S3 → RGB LED (via 220Ω resistors)

| XIAO Pin | LED Leg |
|----------|---------|
| GPIO7 | Blue |
| GPIO8 | Red |
| GPIO9 | Green |
| GND/13 | Common leg → GND |

### XIAO ESP32-S3 → Buttons

| XIAO Pin | Button |
|----------|--------|
| GPIO5 | Button 1 (other leg → GND) |
| GPIO6 | Button 2 (other leg → GND) |

### Power & Ground

| XIAO Pin | Connects To |
|----------|-------------|
| 3.3V | L293D VCC1 (Pin 16), EN1,2 (Pin 1), EN3,4 (Pin 9) |
| 5V | L293D VCC2 (Pin 8), Motor Red wire |
| GND | L293D GND (Pins 4, 5, 12, 13), LED common leg, both buttons |

## Bill of Materials

| Part | Qty | Source | Unit Cost | Notes |
|------|-----|--------|-----------|-------|
| Seeed XIAO ESP32-S3 | 1 | Digikey | $7.49 | Main microcontroller |
| L293D H-bridge driver | 1 | Digikey | $8.86 | Level-shifts 3.3V logic to 5V motor power |
| 28BYJ-48 stepper motor | 1 | Adafruit | $4.95 | Drives clock hand; no clean single-unit listing found |
| RGB LED (common cathode, 4-pin) | 1 | Digikey | $2.66 | PWM-driven, indicates timer state |
| Tactile switch | 2 | Digikey | $0.10 | Button 1 (preset select), Button 2 (start/pause/reset) |
| 220Ω resistor | 3 | Digikey | $0.10| LED current limiting |
| USB-C cable | 1 | — | — | Power + programming |
| Popsicle stick | 1 | — | — | Clock hand |
| Jumper wires | — | — | — | Breadboard connections |
