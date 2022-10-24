#include "DHT.h"

#define DHTPIN 3
DHT dht(DHTPIN, DHT11);
const int movPin = 2;
uint32_t timer_log;
void setup() {
    Serial.begin(9600);
    pinMode(movPin, INPUT);
    dht.begin();
}

void loop(){
    int val = digitalRead(movPin);
  //  Serial.println(val);

    delay(300);


  float h = dht.readHumidity(); 
  float t = dht.readTemperature(); 


        if (val == 1)
    {
      Serial.println("*alert*"); // alert for camera
      delay(2000);
    }

          
         
           if (millis() - timer_log >= 5000)
           {
              Serial.print("Влажность: ");
              Serial.print(h);
              Serial.print(" %\t");
              Serial.print("Температура: ");
              Serial.print(t);
              Serial.println(" *C "); 
              timer_log = millis();
            }
          
      
}
