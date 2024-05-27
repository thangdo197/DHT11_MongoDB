#include <DHT.h>
#define DHTPIN 2
#define IRPIN 3

#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);

void setup(){
  Serial.begin(9600);
  dht.begin();
  pinMode(IRPIN, OUTPUT);
}

void loop(){
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  bool irStatus = digitalRead(IRPIN);

  Serial.print('Temperature: ');
  Serial.print(temp);
  Serial.print('°C, Humidity: ');
  Serial.print(hum);
  Serial.print('%, IR status: ');
  Serial.println(irStatus ? 'on' : 'off');

  delay(500);
}
