#include <Servo.h>

Servo motor;
//pin number
int potPin = A0;     
int servoPin = 6;     
int ledPin = 5;      

int volt;
int angle;

void setup() {

  motor.attach(servoPin);
  pinMode(ledPin, OUTPUT);

}

void loop() {

  // read potentiometer value
  volt = analogRead(potPin);

  // convert value to angle
  angle = map(volt, 0, 1023, 0, 180);

  // check  limit
  if(angle > 68) {

    motor.write(68);        
    digitalWrite(ledPin, HIGH);  

  } 
   // normal movement
  else {

    motor.write(angle);    
    digitalWrite(ledPin, LOW);   

  }

  delay(20);
}