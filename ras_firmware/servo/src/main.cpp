#include <Arduino.h>
#include <Servo.h>

unsigned int SERVO_PIN = 9;

Servo servo = Servo();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  servo.attach(SERVO_PIN);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    int x = Serial.parseInt();

    if(x >= 0 && x <180)
      servo.write(x);
  }
  delay(10);
}
