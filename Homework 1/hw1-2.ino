int photocellPin = 2; // Photocell on analog in A2
int resistiity = 0;   // Light resistance variable
int minLight = 700;   // Light threshold
int led = 9;          // led pin
int ledState = 0;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  resistiity = analogRead(photocellPin);
  Serial.println(resistiity);

  if (resistiity < minLight && ledState == 0) {
    digitalWrite(led, HIGH); // turn on LED
    ledState = 1;
  }

  if (resistiity > minLight && ledState == 1) {
    digitalWrite(led, LOW); // turn off LED
    ledState = 0;
  }

  delay(100);
}
