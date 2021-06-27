#include "ESP8266WiFi.h"
#include "ESP8266WiFiMulti.h"
ESP8266WiFiMulti WiFiMulti;
#define wifi_id "MEIKO   3F"
#define wifi_pass "0932154760"

#include <DHT.h>

#define dhtPin 12
#define dhtType DHT11
DHT dht(dhtPin, dhtType);

const int ledPin = 13;

void setup() {
  Serial.begin(115200);
  dht.begin(); // DHT Start

  pinMode(ledPin, OUTPUT);

  WiFiMulti.addAP(wifi_id, wifi_pass);

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.println("wait...");
    delay(500);
  }
}

void loop() {
  if (!dht.read(dhtPin)) {
    Serial.println("無法從DHT傳感器讀取！");
    return;
  }
  int l = random(100) % 2;
  if (l) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("% // ");
  Serial.print("Celsius: ");
  Serial.print(t);
  Serial.print("℃ // ");
  Serial.print("LED: ");
  Serial.print(l);

  const uint16_t port = 80;
  const char *host = "192.168.52.80";
  Serial.print("連線至[");
  Serial.print(host);
  Serial.println("]");

  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("connect failed");
    Serial.println("wait 3 sec...");
    delay(3000);
    return;
  }

  String url =
      "/addData.php?t=" + String(t) + "&h=" + String(h) + "&l=" + String(l);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" + "Host: " + host +
               "\r\n" + "Connection: Close\r\n\r\n");

  Serial.println("connect closed");
  client.stop();
  delay(5000);
}
