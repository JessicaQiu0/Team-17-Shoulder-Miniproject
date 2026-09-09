# Electrical

## Contents

| File | Description |
|------|-------------|
| `Electric_Schematic.pdf` | Full circuit schematic |
| `SeniorDesign_MiniProject_Schematic.kicad_sch` | Editable KiCad source file |

## Overview

XIAO ESP32-S3 microcontroller drives an L293D H-bridge to control a 28BYJ-48 unipolar stepper motor (wave-pulse sequencing), plus a common-cathode RGB LED (PWM-controlled, 220Ω current-limiting resistors) and 2 push buttons for user input.

## Pin Mapping

| XIAO Pin | Connects To |
|----------|-------------|
| GPIO1-4 | L293D inputs 1A-4A → motor coils |
| GPIO5, GPIO6 | Buttons 1, 2 |
| GPIO7, GPIO8, GPIO9 | RGB LED (R, B, G) via 220Ω resistors |
