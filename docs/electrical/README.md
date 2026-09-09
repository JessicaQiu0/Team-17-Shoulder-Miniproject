# Electrical

## Contents

| File | Description |
|------|-------------|
| `SeniorDesign_MiniProject_Schematic.pdf` | Full circuit schematic |
| `SeniorDesign_MiniProject_Schematic.kicad_sch` | Editable KiCad source file |

## Overview

XIAO ESP32-S3 microcontroller drives an L293D H-bridge to control a 28BYJ-48 unipolar stepper motor (wave-pulse sequencing), plus a common-cathode RGB LED (PWM-controlled, 220Ω current-limiting resistors) and 2 push buttons for user input.

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
| GPIO7 | Red |
| GPIO8 | Blue |
| GPIO9 | Green |
| — | Common leg → GND |

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
