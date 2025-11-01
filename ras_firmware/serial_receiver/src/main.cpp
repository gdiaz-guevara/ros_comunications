#include <Arduino.h>

unsigned int BUILT_LED = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(BUILT_LED, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available())
  {
    int x = Serial.parseInt();

    if (x == 1)
      digitalWrite(BUILT_LED, HIGH);
    else
      digitalWrite(BUILT_LED, LOW);
  }

  delay(10);
}
