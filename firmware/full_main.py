# mini project code in minutes
import time
from machine import PWM, Pin

# pins
motor = [Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]

button1 = Pin(5, Pin.IN, Pin.PULL_UP)
button2 = Pin(6, Pin.IN, Pin.PULL_UP)

# led wiring
blue = PWM(Pin(7))
red = PWM(Pin(8))
green = PWM(Pin(9))

blue.freq(1000)
red.freq(1000)
green.freq(1000)

# motor
sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

step_index = 0
current_position = 0

# 30 minutes is one full rotation
FULL_30_MIN_STEPS = 2048


def single_step(direction):
  global step_index
  global current_position

  # change direction to negative to rotate the right way
  actual_direction = -direction

  step_index = (step_index + actual_direction) % 4
  step = sequence[step_index]

  for pin, value in zip(motor, step):
    pin.value(value)

  current_position += direction
  time.sleep_ms(5)


def motor_off():
  for pin in motor:
    pin.value(0)


def minutes_to_steps(minutes):
  return int(FULL_30_MIN_STEPS * minutes / 30)


def move_to_minutes(minutes):
  global current_position

  target = minutes_to_steps(minutes)

  while current_position < target:
    single_step(1)

  while current_position > target:
    single_step(-1)

  motor_off()


# presets that are pre allocated
presets = [15, 20, 25, 30]

preset_index = -1
selected_minutes = 0

remaining_ms = 0
total_time_ms = 0
last_update = 0

# states of the timer
SELECTING = 0
RUNNING = 1
PAUSED = 2
FINISHED = 3

state = SELECTING


# leds
def leds_off():
  red.duty_u16(0)
  green.duty_u16(0)
  blue.duty_u16(0)


def update_leds():
  cycle = time.ticks_ms() % 1000

  if cycle < 500:
    brightness = int(cycle / 500 * 65535)
  else:
    brightness = int((1000 - cycle) / 500 * 65535)

  leds_off()

  # blue state is when selecting or paused
  if state == SELECTING or state == PAUSED:
    blue.duty_u16(brightness)
  # green state is when running
  elif state == RUNNING:
    green.duty_u16(brightness)
  # red state is when finished
  elif state == FINISHED:
    red.duty_u16(brightness)


### preset selection
def next_preset():
  global preset_index
  global selected_minutes
  global remaining_ms
  global total_time_ms

  preset_index = (preset_index + 1) % len(presets)
  selected_minutes = presets[preset_index]

  # NOTE TO SELF:
  # delete the *60 if you want it to move in terms of seconds for testing purposes
  total_time_ms = selected_minutes * 60 * 1000
  remaining_ms = total_time_ms

  print('selected:', selected_minutes, 'minutes')

  # move hand to the selected physical position
  move_to_minutes(selected_minutes)


### timer control
def start_timer():
  global state
  global last_update

  state = RUNNING
  last_update = time.ticks_ms()
  print('countdown started')


def pause_timer():
  global state

  state = PAUSED
  motor_off()
  print('paused')


def resume_timer():
  global state
  global last_update

  state = RUNNING
  last_update = time.ticks_ms()
  print('resumed')


def reset_timer():
  global state
  global remaining_ms
  global total_time_ms
  global selected_minutes
  global preset_index

  print('resetting to 0')

  # return hand to zero
  move_to_minutes(0)

  # clear the selected timer
  remaining_ms = 0
  total_time_ms = 0
  selected_minutes = 0
  preset_index = -1

  state = SELECTING

  print('reset complete')
  print('hand at 0')
  print('select a new preset')


### countdown
def update_timer():
  global remaining_ms
  global last_update
  global state
  global current_position

  if state != RUNNING:
    return

  now = time.ticks_ms()
  elapsed = time.ticks_diff(now, last_update)
  last_update = now

  remaining_ms -= elapsed

  # timer finished
  if remaining_ms <= 0:
    remaining_ms = 0
    while current_position > 0:
      single_step(-1)
    motor_off()
    state = FINISHED
    print('time is up!!!')
    return

  # percentage of time remaining
  fraction_remaining = remaining_ms / total_time_ms

  # original physical preset position
  starting_position = minutes_to_steps(selected_minutes)

  # move gradually toward 0
  target_position = int(starting_position * fraction_remaining)

  if current_position > target_position:
    single_step(-1)
    motor_off()


### button 1 code
def handle_button1():
  if state != SELECTING:
    return

  if button1.value() == 0:
    time.sleep_ms(30)
    if button1.value() == 0:
      next_preset()
      while button1.value() == 0:
        update_leds()
        time.sleep_ms(10)
      time.sleep_ms(30)


### button 2 code
def handle_button2():
  global state

  if button2.value() != 0:
    return

  time.sleep_ms(30)
  if button2.value() != 0:
    return

  press_start = time.ticks_ms()
  while button2.value() == 0:
    update_leds()
    held_time = time.ticks_diff(time.ticks_ms(), press_start)

    # hold for 2 seconds to reset to zero
    if held_time >= 2000:
      reset_timer()
      while button2.value() == 0:
        time.sleep_ms(10)
      return
    time.sleep_ms(10)

  time.sleep_ms(30)

  # short press
  if state == SELECTING:
    if selected_minutes > 0:
      start_timer()
    else:
      print('select a preset first')
  elif state == RUNNING:
    pause_timer()
  elif state == PAUSED:
    resume_timer()
  elif state == FINISHED:
    reset_timer()


### startup code
leds_off()
motor_off()

print()
print('meeting timer')
print()

# this line assumes the hand is physically at 15 when code starts
current_position = minutes_to_steps(15)

print('returning hand from 15 to 0')
move_to_minutes(0)

print('hand is at 0')
print()
print('button 1 = select 15 / 20 / 25 / 30 minutes')
print('button 2 = start / pause / resume')
print('hold button 2 = reset to 0')
print()

# main loop
while True:
  update_leds()
  handle_button1()
  handle_button2()
  update_timer()
  time.sleep_ms(5)