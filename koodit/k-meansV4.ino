#include "centerpoints.h"
#include "accelerator.h"

void setup()
{
  //Accelerometer setup
// TRANSMITTER DIGITAL 12
// RECEIVER DIGITAL 11
  pinMode(A0, OUTPUT);
  digitalWrite(A0, HIGH);   //POWER

  pinMode(A4, OUTPUT);
  digitalWrite(A4, LOW);    //GROUND

  Serial.begin(9600);
}

//muuttujien alustusta
int state =1;
int distances[]={0,0,0,0,0,0};
int dif1,dif2,dif3,pointSum,P,minVal;

//etaisuus funktio

int distance3D(int sV1,int sV2,int sV3,int cP1,int cP2,int cP3){
  dif1= sV1-cP1;
  dif2= sV2-cP2;
  dif3= sV3-cP3;
  pointSum=(dif1*dif1)+(dif2*dif2)+(dif3*dif3);
  P =sqrt(pointSum);
  return P;
}



//pää looppi
void loop() {

switch (state)  {
  case 1: //mittaus
    delay(10);
  
    Accelerator Aobject;
    Aobject.makeMeasurement();
    Measurement a = Aobject.getMeasurement();

    Serial.print("Sensoriarvot: X: ");
    Serial.print(a.x);
    Serial.print(" Y: ");
    Serial.print(a.y);
    Serial.print(" Z: ");
    Serial.println(a.z);
    
    state = 2;
  
  
  case 2: //lasku
    
    distances[5]=distance3D(a.x,a.y,a.z,cP[0],cP[1],cP[2]);
    distances[2]=distance3D(a.x,a.y,a.z,cP[3],cP[4],cP[5]);
    distances[0]=distance3D(a.x,a.y,a.z,cP[6],cP[7],cP[8]);
    distances[3]=distance3D(a.x,a.y,a.z,cP[9],cP[10],cP[11]);
    distances[1]=distance3D(a.x,a.y,a.z,cP[12],cP[13],cP[14]);
    distances[4]=distance3D(a.x,a.y,a.z,cP[15],cP[16],cP[17]);

int count = sizeof(distances) / sizeof(distances[0]);
int index = 0 ; 

for (int i = 1; i < count; i++)
{
if (distances[i] < distances[index]) {
index = i;
}
}

switch (index){
  case 0:
  Serial.println("Arduino on kohti kattoa!!");
  break;

  case 1:
  Serial.println("Arduino on kohti lattiaa!!");
  break;

  case 2:
  Serial.println("Arduino on kohti vasenta!!");
  break;

  case 3:
  Serial.println("Arduino on kohti oikeaa!!");
  break;

  case 4:
  Serial.println("Arduino on käännetty eteenpäin!!");
  break;

  case 5:
  Serial.println("Arduino on kohti itseä!!");
  break;
  
  }
    
    state = 1; 
    delay(1000);
}
}
