int led = 13;
int initial = 2000;
int interval = initial;
int delta = 100;
char cmd;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

// loop
void loop() {
  Serial.println("Current interval is ");
  Serial.println(interval);
  if (Serial.available() > 0)
    cmd = Serial.read();

  switch (cmd) {
  case '+':
    if (interval >= delta)
      interval -= delta;
    else {
      Serial.print("Current interval is ");
      Serial.println(interval);
      Serial.print("Current interval is min. ");
    };
    break;

  case '-':
    if (interval < initial)
      interval += delta;
    else {
      Serial.print("Current interval is ");
      Serial.println(interval);
      Serial.print("Current interval is max. ");
    };
    break;

  default:
    Serial.println("input + or - only.");
  }
  digitalWrite(led, HIGH);
  delay(interval);
  digitalWrite(led, LOW);
  delay(interval);
}
