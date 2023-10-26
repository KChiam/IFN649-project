const int buzzer = 14; //Pin assignment for buzzy buzzer

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  
  // Setup Serial1 for Bluetooth (Tier 2)
  Serial1.begin(9600); // Default communication rate of the Bluetooth module

  // Setup buzzy buzzer
  pinMode(buzzer, OUTPUT); //initialising pin mode for output of power to LED (for it to turn on (3.3V) and off (0V)
}

//Turn the pin on or off depending on the data received via bluetooth as above
void loop() {
  if(Serial1.available() > 0){ // Checks whether data is comming from the serial port
        
    //Buzzer - receive command for buzzer
    String str = Serial1.readString().substring(0); //substring 0 because you read the FIRST character 

    //turn the pin on or off depending on the data received via bluetooth as above
    Serial.println(str);
    if(str == "safe"){
    tone(buzzer, 2000,250); //beep at 1000 freq for 250ms
    delay(500); //stop beeping for 500 ms
    tone(buzzer, 2000,250); //beep at 1000 freq for 250ms
    Serial.println("Consume, my Lord"); //you need humour to get through this

    } else if(str == "notsafe"){
    tone(buzzer,2000, 2500); //beep at 500freq for 2500ms/2.5s
    Serial.println("A CAULDRON!"); //you need humour to get through this
    }
  }
}

