#include <Arduino.h>
#include <module2/module2.h>

void setup() {
  Module2 m2 = Module2();
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  Serial.println("hello from exec node");
  digitalToggle(LED_BUILTIN);
  delay(1000);
}