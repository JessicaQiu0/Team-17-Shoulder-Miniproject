
import time
from machine import PWM, Pin
import stepper_driver as driver

# Input switches
button1 = Pin(5, Pin.IN, Pin.PULL_UP)
button2 = Pin(6, Pin.IN, Pin.PULL_UP)

# PWM outputs with official pin assignments
red_led = PWM(Pin(7))
blue_led = PWM(Pin(8))
green_led = PWM(Pin(9))

for led in (red_led, blue_led, green_led):
  led.freq(1000)

# Operational states
SELECTING = 0
RUNNING = 1
PAUSED = 2
FINISHED = 3

state = SELECTING
presets = [15, 20, 25, 30]
preset_index = -1
selected_minutes = 0

remaining_ms = 0
total_time_ms = 0
last_update = 0


def leds_off():
  red_led.duty_u16(0)
  blue_led.duty_u16(0)
  green_led.duty_u16(0)


def update_led_breathing():
  cycle = time.ticks_ms() % 1000
  brightness = (
      int(cycle / 500 * 65535)
      if cycle < 500
      else int((1000 - cycle) / 500 * 65535)
  )
  leds_off()

  if state in (SELECTING, PAUSED):
    blue_led.duty_u16(brightness)
  elif state == RUNNING:
    green_led.duty_u16(brightness)
  elif state == FINISHED:
    red_led.duty_u16(brightness)


def next_preset():
  global preset_index, selected_minutes, remaining_ms, total_time_ms
  preset_index = (preset_index + 1) % len(presets)
  selected_minutes = presets[preset_index]
  total_time_ms = selected_minutes * 60 * 1000
  remaining_ms = total_time_ms
  print('Selected:', selected_minutes, 'minutes')
  driver.sweep_to_position(driver.minutes_to_steps(selected_minutes))


def reset_timer():
  global state, remaining_ms, total_time_ms, selected_minutes, preset_index
  driver.sweep_to_position(0)
  remaining_ms = 0
  total_time_ms = 0
  selected_minutes = 0
  preset_index = -1
  state = SELECTING
  print('Reset complete: Pointer homed to 0')


def update_countdown():
  global remaining_ms, last_update, state
  if state != RUNNING:
    return

  now = time.ticks_ms()
  elapsed = time.ticks_diff(now, last_update)
  last_update = now
  remaining_ms -= elapsed

  if remaining_ms <= 0:
    remaining_ms = 0
    driver.sweep_to_position(0)
    state = FINISHED
    print('Countdown Expired!')
    return

  fraction_remaining = remaining_ms / total_time_ms
  start_pos = driver.minutes_to_steps(selected_minutes)
  target_pos = int(start_pos * fraction_remaining)

  if driver.get_current_position() > target_pos:
    driver.single_step(-1)
    driver.deenergize_coils()


def handle_inputs():
  global state, last_update
  # Button 1: Preset cycling with active-low debounce
  if state == SELECTING and button1.value() == 0:
    time.sleep_ms(30)
    if button1.value() == 0:
      next_preset()
      while button1.value() == 0:
        update_led_breathing()
        time.sleep_ms(10)
      time.sleep_ms(30)

  # Button 2: Short press toggle / Long press reset
  if button2.value() == 0:
    time.sleep_ms(30)
    if button2.value() == 0:
      press_start = time.ticks_ms()
      while button2.value() == 0:
        update_led_breathing()
        if time.ticks_diff(time.ticks_ms(), press_start) >= 2000:
          reset_timer()
          while button2.value() == 0:
            time.sleep_ms(10)
          return
        time.sleep_ms(10)
      time.sleep_ms(30)

      if state == SELECTING and selected_minutes > 0:
        state = RUNNING
        last_update = time.ticks_ms()
      elif state == RUNNING:
        state = PAUSED
        driver.deenergize_coils()
      elif state == PAUSED:
        state = RUNNING
        last_update = time.ticks_ms()
      elif state == FINISHED:
        reset_timer()


def run_timer():
  leds_off()
  driver.deenergize_coils()
  driver.sweep_to_position(driver.minutes_to_steps(15))
  driver.sweep_to_position(0)

  while True:
    update_led_breathing()
    handle_inputs()
    update_countdown()
    time.sleep_ms(5)