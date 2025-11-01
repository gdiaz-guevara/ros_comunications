#include <Arduino.h>

int counter = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(counter);
  counter++;
  delay(100);
}
