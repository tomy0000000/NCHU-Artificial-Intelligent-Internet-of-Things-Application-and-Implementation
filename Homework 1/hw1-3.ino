#include <DHT.h>

#define dhtPin 8
#define dhtType DHT11
DHT dht(dhtPin, dhtType);

void setup() {
  Serial.begin(9600);
  dht.begin(); // DHT Start
}

void loop() {

  if (!dht.read(dhtPin)) {
    Serial.println("無法從DHT傳感器讀取！");
    return;
  } else {
    Serial.print("Humidity: ");
    Serial.print(dht.readHumidity());
    Serial.print("% // ");
    Serial.print("Celsius: ");
    Serial.print(dht.readTemperature());
    Serial.print("℃ // ");
    Serial.print("Fahrenheit: ");
    Serial.print(dht.readTemperature(true));
    Serial.print("℉\n");
  }

  delay(1000);
}
