# Low-level stepper motor hardware driver and GPIO interface for Seeed XIAO ESP32-S3.

import time
from machine import Pin

# Define discrete digital outputs to L293D inputs
motor_pins = [
    Pin(1, Pin.OUT),  # 1A -> Pin 2
    Pin(2, Pin.OUT),  # 2A -> Pin 7
    Pin(3, Pin.OUT),  # 3A -> Pin 10
    Pin(4, Pin.OUT),  # 4A -> Pin 15
]

# 4-phase wave drive excitation sequence (one coil energized at a time)
WAVE_SEQUENCE = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# 28BYJ-48 gear ratio and resolution calibration
FULL_ROTATION_STEPS = 2048  # 360-degree rotation constant
step_index = 0
current_position = 0


def single_step(direction):
  """Advance the motor by a single wave step with reversed polarity correction."""
  global step_index, current_position
  actual_direction = -direction
  step_index = (step_index + actual_direction) % len(WAVE_SEQUENCE)
  step_pattern = WAVE_SEQUENCE[step_index]

  for pin, state in zip(motor_pins, step_pattern):
    pin.value(state)

  current_position += direction
  time.sleep_ms(5)


def deenergize_coils():
  """Set all coil pins to 0 to eliminate static holding current and thermal dissipation."""
  for pin in motor_pins:
    pin.value(0)


def minutes_to_steps(minutes, dial_span_minutes=30):
  """Convert time in minutes to target step position across dial geometry."""
  return int(FULL_ROTATION_STEPS * (minutes / dial_span_minutes))


def sweep_to_position(target_steps):
  """Sweep pointer arm to absolute angular step coordinate."""
  global current_position
  while current_position < target_steps:
    single_step(1)
  while current_position > target_steps:
    single_step(-1)
  deenergize_coils()


def get_current_position():
  return current_position
