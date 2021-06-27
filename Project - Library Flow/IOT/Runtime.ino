#include "scanning.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <SoftwareSerial.h>

SoftwareSerial BTserial(D7, D8); // (RX, TX)

#define SERVER_IP "SEVER IP"

#ifndef STASSID
#define STASSID "SSID"
#define STAPSK  "PWD"
#endif

char c = ' ';

void setup() {

  Serial.begin(115200);
  Serial.println();
  Serial.println();
  Serial.println();

  WiFi.begin(STASSID, STAPSK);
  BTserial.begin(38400);

  // Wait for hardware to initialize
  delay(1000);

  // Set correct states for inq
  initHC05ToInq();

  // Start inq
  initMessage();
  BTserial.println("AT+INQ");

  // Connecting to Wifi...
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  
  int num = random(50);
  // wait for WiFi connection
  if ((WiFi.status() == WL_CONNECTED)) {
    WiFiClient client;
    HTTPClient http;

    prepareJson();
    // String jsonStr = "{\"section_id\": 1,\"status\":" + (String)num + "}";
    Serial.println(send);
    String jsonStr = send;
    Serial.print("[HTTP] begin...\n");
    // configure traged server and url
    http.begin(client, "http://" SERVER_IP "/record"); //HTTP
    http.addHeader("accept", "application/json");
    http.addHeader("Content-Type", "application/json");
    http.addHeader("Content-Length", String((jsonStr.length() + 6)) );

    Serial.print("[HTTP] POST...\n");
    // start connection and send HTTP header and body
    int httpCode = http.POST(jsonStr);
    if (httpCode > 0) {
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);
      if (httpCode == HTTP_CODE_OK) {
        const String& payload = http.getString();
        Serial.println("received payload:\n<<");
        Serial.println(payload);
        Serial.println(">>");
      }
    }else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
  }
  delay(300000);
}
