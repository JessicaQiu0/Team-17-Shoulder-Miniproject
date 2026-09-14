# Mechanical

## Contents

| File              | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| `Box.stl`         | 3D-printable enclosure body                                    |
| `Assembly 1.stl`  | Complete enclosure assembly for visualization and fit checking |
| `Box Drawing.dxf` | 2D drawing of the enclosure body                               |
| `Lid Drawing.dxf` | 2D drawing of the enclosure lid                                |
| `Lid DXF.dxf`     | Clock face design used for engraving the lid                   |
| `Pointer.dxf`     | DXF used to cut popsicle stick                                 |


## Overview

The mechanical design consists of a 3D-printable enclosure and lid that house the timer's electrical components and support the stepper motor used to drive the mechanical countdown display.

The enclosure was designed to keep the overall construction simple while providing the necessary mounting and access features for the electronics. The design includes a pathway for the external USB-C cable and a secure mounting location for the stepper motor.

To give the device the appearance of a physical clock rather than a generic electronics enclosure, the team decided to use a clock-inspired aesthetic. A clock face was added to the lid as an engraving, with the stepper motor positioned so that its shaft can drive the external clock hand. The popsicle stick was laser cut to be shorter to accommodate the LED and have a tip that aligns with the clock ticks.

## Enclosure Design

### Box

The box forms the main body of the enclosure and provides space for the microcontroller, motor driver, wiring, and other electrical components.

The enclosure was designed with the following considerations:

* Sufficient internal space for the electrical components and wiring
* A pathway for the USB-C cable for power and programming
* Simple geometry to make the enclosure easy to manufacture and assemble
* Compatibility with the separate lid

The printable enclosure geometry is provided in `Box.stl`, while `Box Drawing.dxf` contains the corresponding 2D drawing.

### Lid

The lid closes the enclosure and serves as the visible clock face of the timer. It includes the features needed to integrate the mechanical countdown display with the enclosure.

The lid was designed to:

* Support the stepper motor securely
* Allow the motor shaft to extend through the lid and connect to the clock hand
* Provide a clock-style front face for the timer
* Fit with the main enclosure for assembly

The lid drawing is provided in `Lid Drawing.dxf`.

## Clock Face

The team decided to give the enclosure a clock-inspired appearance to better communicate the timer's function.

A clock face design was created for engraving onto the lid. This adds numerical markings directly to the enclosure rather than requiring separate labels or components.

The engraving geometry is provided in `Lid DXF.dxf`.

## Stepper Motor Integration

The enclosure is designed around the 28BYJ-48 stepper motor used for the timer's mechanical countdown display.

The motor is mounted to the lid so that its output shaft passes through the clock face. A clock hand can then be attached to the shaft and rotated as the timer counts down.

The motor mounting geometry was designed to keep the motor securely positioned and aligned with the center of the clock face.

## Assembly

The complete enclosure consists of the box, lid, stepper motor, internal electronics, and external clock hand.

`Assembly 1.stl` provides the assembled geometry and can be used to visualize the completed enclosure and verify the relationship between the individual mechanical components.

## Manufacturing and Assembly Notes

The box and lid are designed to be 3D printed as separate components.

Before final assembly:

1. Check that the stepper motor fits correctly in its mounting location.
2. Verify that the motor shaft is aligned with the center of the clock face.
3. Confirm that the USB-C cable can pass through the enclosure without interference.
4. Install the electrical components and route the wiring inside the enclosure.
5. Attach the lid to the enclosure.
6. Attach the clock hand to the stepper motor shaft.

The clock face engraving should be added to the lid before final assembly.

