#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  Serial.println("hello from brain node");
  digitalToggle(LED_BUILTIN);
  delay(50);
}