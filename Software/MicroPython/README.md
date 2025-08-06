# Getting Started with MicroPython

This folder contains a few example programs with in MicroPython to be used on
a **M5Stack Atom Lite** or **M5Stack Atom S3 Lite** as the microcontroller
attached to the LuxCamp badge.

## Prerequisites

1. Flash the correct MicroPython to the AtomLite using one of the following guides:
  - MicroPython for [Atom Lite (grey case)](https://micropython.org/download/M5STACK_ATOM/)
  - MicroPython for [Atom S3 Lite (white case)](https://micropython.org/download/M5STACK_ATOMS3_LITE/
  )
2. Install [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)
   for accessing the MicroPython console and filesystem on the Atom Lite.

> *Note*: These example programs have been tested against MicroPython v1.25.0.

Once MicroPython has been flashed onto the Atom Lite, verify that the installation
succeeded by using the following command to get access to the console:

```console
$ mpremote repl
Connected to MicroPython at /dev/ttyACM0
Use Ctrl-] or Ctrl-x to exit this shell
MicroPython v1.25.0 on 2025-04-15; M5Stack AtomS3 Lite with ESP32S3
Type "help()" for more information.
>>>
```

## Running the `SimpleTouch` example

The `SimpleTouch` program is the easiest way to familiarize yourself with the
capabilities of the badge.

Before you can run the `SimpleTouch` program (and other examples using the touch
sensor), make sure to install the MPR121 driver module on the Atom Lite first.
Copy it to Atom Lite using the following command:

```console
$ mpremote fs cp mpr121.py :
```

You can then run the `SimpleTouch` example using the following command. You
should see a welcome message as follows:

```console
$ mpremote run SimpleTouch/main.py

LuxCamp Badge 2025 - SimpleTouch is running...
Hint: Touch the touchpads on the badge to see LEDs light up.
Hint: Press the button on the Atom Lite to stop this program.
```
