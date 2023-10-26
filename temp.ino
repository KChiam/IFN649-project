#include "DHT.h"
//#include <SoftwareSerial.h>

#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
#define LEDPIN 11

DHT dht(DHTPIN, DHTTYPE);


// Teensy 5V <--> HC-05 Vcc
// Teensy Ground <--> HC-05 GND
#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  // Setup DHT Sensor
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for Bluetooth (Tier 2)
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
}


void loop() {

//DHT Sensor - sending temp data with DHT Sensor
    float t = dht.readTemperature();
    digitalWrite(LEDPIN, HIGH);
    
    Serial.println(t); //print on Arduino
    Serial1.println(t); //print on Raspberry Pi
    
    delay(1000);
    digitalWrite(LEDPIN, LOW);
    delay(1000);
}
