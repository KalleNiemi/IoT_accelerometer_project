#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
  // Serial.println("Accelerator created!");
}


Accelerator::~Accelerator()
{
   //Serial.println("Accelerator deleted!");
}

void Accelerator::makeMeasurement()
{
  m.x = analogRead(A1);
  m.y = analogRead(A2);
  m.z = analogRead(A3);
  
}
Measurement Accelerator::getMeasurement()
{
 return m;
}
