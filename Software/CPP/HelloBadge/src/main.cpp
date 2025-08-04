#include <Arduino.h>
#include <M5Unified.h>
#include "Adafruit_MPR121.h"
#include <Adafruit_NeoPixel.h>

#define LED_COUNT 72

#ifdef BOARD_ATOM
  #define DataPin 19
  #define BuiltinLED 27
  #define SDAPin 25
  #define SCLPin 21
#endif
#ifdef BOARD_ATOMS3
  #define DataPin 6
  #define BuiltinLED 35
  #define SDAPin 38
  #define SCLPin 39
#endif

Adafruit_NeoPixel strip(LED_COUNT, DataPin, NEO_GRB + NEO_KHZ800);
Adafruit_MPR121 cap = Adafruit_MPR121();

uint16_t lasttouched = 0;
uint16_t currtouched = 0;

void setup() {
  
  auto cfg = M5.config();
  
  M5.begin(cfg);
  M5.Power.setLed(0);
  
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)

  Serial.begin(115200);

  Serial.println("LEDs initialized");
  
  Serial.println("Starting MPR121");
  Wire.begin(SDAPin,SCLPin,4000000);
  if (!cap.begin(0x5A)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
  cap.setAutoconfig(true);
  Serial.println("MPR121 found!");
}


int hue=0;
int value=0;
int direction = 10;

void loop() {
  // put your main code here, to run repeatedly:
  M5.update();

    value += direction;
    if (value <= 100) {
      direction = 10;
      value = 100;
    } else if (value >= 255) {
      direction = -10;
      value = 255;
    }
    uint32_t color = strip.ColorHSV(hue * 65536 / 360, 255, value);
    for (int i=0;i<LED_COUNT;i++){
      strip.setPixelColor(i,color);
    }
    strip.show();
    delay(50);

    // Get the currently touched pads
  currtouched = cap.touched();
  
  for (uint8_t i=0; i<12; i++) {
    // it if *is* touched and *wasnt* touched before, alert!
    if ((currtouched & _BV(i)) && !(lasttouched & _BV(i)) ) {
      Serial.print(i); Serial.println(" touched");
      hue = (i * 20) % 255; // Change hue based on the pad touched
    }
    // if it *was* touched and now *isnt*, alert!
    if (!(currtouched & _BV(i)) && (lasttouched & _BV(i)) ) {
      Serial.print(i); Serial.println(" released");
    }
  }

  // reset our state
  lasttouched = currtouched;

  /*
  // debugging info, what
  Serial.print("\t\t\t\t\t\t\t\t\t\t\t\t\t 0x"); Serial.println(cap.touched(), HEX);
  Serial.print("Filt: ");
  for (uint8_t i=0; i<12; i++) {
    Serial.print(cap.filteredData(i)); Serial.print("\t");
  }
  Serial.println();
  Serial.print("Base: ");
  for (uint8_t i=0; i<12; i++) {
    Serial.print(cap.baselineData(i)); Serial.print("\t");
  }
  Serial.println();
  
  // put a delay so it isn't overwhelming
  delay(100);
  */

}
