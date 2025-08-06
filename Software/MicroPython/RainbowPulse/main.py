import machine, neopixel, os, time

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

num_leds = 72
btn = machine.Pin(PIN_BTN, machine.Pin.IN, machine.Pin.PULL_UP)
np = neopixel.NeoPixel(PIN_LED, num_leds)

def wheel(pos):
    """Generate RGB values from a color wheel position (0-255)."""
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

offset = 0
while btn.value():
    for i in range(num_leds):
        # Get next color from color wheel
        color = wheel((i + offset) % 256)
        # Reduce brightness to 20%
        np[i] = tuple([c // 5 for c in color])
    np.write()
    offset = (offset + 1) % 256
    time.sleep_ms(50)

