#include "DHT.h"
#include <FirebaseArduino.h>
#include <ESP8266WiFi.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

 
#define FIREBASE_HOST "my-project-1557998794910.firebaseio.com"
#define FIREBASE_AUTH "Y8YBdXECVTDgQjP9xUnwx9lqzxxPrh4jv4zgXN9t"
#define WIFI_SSID "Sparta"
#define WIFI_PASSWORD "titan987"




int vibration_sensor=5; // initializing the digital pin


int value;
const int ldrPin = A0;

//long duration;
//int distance;

 String fireStatus;
 String fanStatus;
 
void setup() {

  pinMode(vibration_sensor, INPUT);
  Serial.begin(9600);
  pinMode(ldrPin, INPUT);
dht.begin();
  // connect to wifi.

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
 
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);


}
void loop() {

if (Firebase.failed()) {                          //check for firebase error...
     Serial.print("FIREBASE FAILED...."); 
     Serial.println(Firebase.error());   
     return; 
     delay(1000);
}



 delay(2000);

  float h = dht.readHumidity();
  float t = dht.readTemperature();


 if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }



  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));


   String Temp = String(t);
   Firebase.setString("TEMPERATURE",Temp);


    String Humd = String(h);
    Firebase.setString("HUMIDITY",Humd);
 
//-----
  int ldrStatus = analogRead(ldrPin);
  Serial.print("luminous:");
  Serial.print(ldrStatus);
  String light = String(ldrStatus);    //convert integer humidity to string humidity
  Firebase.setString("LUMINOUS",light);
//---------
//delay(100);
value=pulseIn(vibration_sensor,HIGH); 
Serial.print("   SHOCK:");
Serial.println(value);
String shock = String(value);
Firebase.setString("SHOCK",shock);

  }
