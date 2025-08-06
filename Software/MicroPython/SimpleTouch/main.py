import machine
import mpr121
import time
import neopixel
import os

# The Atom Lite and Atom S3 Lite have different pinouts
if "AtomS3" in os.uname().machine:
    # Atom S3 Lite
    PIN_LED = machine.Pin(6)
    PIN_BTN = machine.Pin(41)
    PIN_SCL = machine.Pin(39)
    PIN_SDA = machine.Pin(38)
else:
    # Atom Lite
    PIN_LED = machine.Pin(19)
    PIN_BTN = machine.Pin(39)
    PIN_SCL = machine.Pin(21)
    PIN_SDA = machine.Pin(25)

num_touchpads = 12
num_leds = 72

# MPR121 is the touch driver
i2c = machine.I2C(scl=PIN_SCL, sda=PIN_SDA)
mpr = mpr121.MPR121(i2c, 0x5A)

# The Atom Lite has a button on the case
btn = machine.Pin(PIN_BTN, machine.Pin.IN, machine.Pin.PULL_UP)

# To use the LEDs, use the neopixel driver
np = neopixel.NeoPixel(PIN_LED, num_leds)

# For each touchpad, define which led LED should light up
touchpad_to_led = [
    35, # Touchpad 0 (backside left top)
    32, # Touchpad 1 (backside left middle)
    30, # Touchpad 2 (backside left bottom)
    29, # Touchpad 3 (front left top)
    28, # Touchpad 4 (front left middle)
    27, # Touchpad 5 (front left bottom)

    63, # Touchpad 6  (front right bottom)
    64, # Touchpad 7  (front right middle)
    65, # Touchpad 8  (front right top)
    66, # Touchpad 9  (backside right bottom)
    68, # Touchpad 10 (backside right middle)
    71, # Touchpad 11 (backside right top)
]

# Each touchpad gets its own color on the color wheel
touchpad_to_color = [
    (255, 0, 0),   # Red
    (255, 85, 0),  # Orange
    (255, 170, 0), # Amber
    (210, 255, 0), # Yellow-Green
    (85, 255, 0),  # Green
    (0, 255, 85),  # Spring Green
    (0, 255, 255), # Cyan
    (0, 170, 255), # Sky Blue
    (0, 85, 255),  # Blue
    (85, 0, 255),  # Indigo
    (170, 0, 255), # Violet
    (255, 0, 170), # Magenta
]

print("LuxCamp Badge 2025 - SimpleTouch is running...")
print("Hint: Touch the touchpads on the badge to see LEDs light up.")
print("Hint: Press the button on the Atom Lite to stop this program.")

while btn.value():
    # Iterate over each touchpad an check if it is touched
    for tp_nr in range(num_touchpads):
        # Get the LED assigned to the touchpad
        led_nr = touchpad_to_led[tp_nr]
        # If touchpad is touched, get the color assigned to the touchpad
        if mpr.is_touched(tp_nr):
            led_color = touchpad_to_color[tp_nr]
        else:
            led_color = (0, 0, 0) # LED off
        # Set new LED color
        np[led_nr] = led_color
    # Update all LEDs at once
    np.write()
    # Sleep for 50 milliseconds
    time.sleep_ms(50)
