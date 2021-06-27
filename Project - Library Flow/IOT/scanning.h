#include <SoftwareSerial.h>
SoftwareSerial BTserial(D7, D8); // (RX, TX)

char c = ' ';

void delayAndRead() {
  delay(50);
  while (BTserial.available()) {
    c = BTserial.read();
  }
  delay(800);
}

void initHC05ToInq() {
  // Enable connect to any device
  BTserial.println("AT+CMODE=0");
  delayAndRead();

  // Set to master in order to enable scanning
  BTserial.println("AT+ROLE=1");
  delayAndRead();

  //RSSI, Max 100 devices, ~30s
  BTserial.println("AT+INQM=1,100,24");
  delayAndRead();

  // COD filter, class=2
  BTserial.println("AT+CLASS=2");
  delayAndRead();

  // Init.
  BTserial.println("AT+INIT");
  delayAndRead();
}

char lineBuffer[100];
char subBuffer[30];
int i = 0;
int index2 = 0;
int total = 0;
bool capture = false;
String send = "";

void initMessage() {
  send = "{\"section_id\": 1, \"devices_list\":[";
}

void prepareJson() {
  
  if(BTserial.available()) {
     c = BTserial.read();
     lineBuffer[i] = c;
     i++;
     if (c == '\n') {
       lineBuffer[i - 1] = 0;
       i = 0;
    
       if (lineBuffer[0] == 'O' && lineBuffer[1] == 'K') {
         send += "]}";
         if (total > 0) {
           Serial.println(send);
         }
         BTserial.println("AT+INQM=1,100,24");
         total = 0;
         initMessage();
       }
       else {
         capture = false;
         index2 = 0;
         for (i = 0; i < 30; i++) {
           if (!capture) {
             if (lineBuffer[i] == ':') {
               capture = true;
             }
           }
           else {
             subBuffer[index2] = lineBuffer[i];
             if (lineBuffer[i] == ',') {
               subBuffer[index2] = 0;
               break;
             }
             index2++;
           }
         }
         i = 0;
         String str((char*)subBuffer);
    
         if (send.indexOf(str) <= 0) {
           if (total > 0) {
             send += ",";
           }
    
           send += "\"";
           send += str;
           send += "\"";
           total++;
         }
       }
     }
  }
}
