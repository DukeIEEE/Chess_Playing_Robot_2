// Open a serial connection and flash LED when input is received

int LED = 4;      // LED connected to digital pin 4
int button = 2;
int x;
int i = 0;
int receive[3];
void setup() {
  // Open serial connection.
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(button, INPUT);
}

void loop() {
  while (Serial.available() > 0) {    // if data present, blink
    receive[i] = Serial.read();
    i++;
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
  }
  if (i > 0) {
    Serial.write("yo dawg1\n");
    Serial.write(receive[2]);
    Serial.write(receive[1]);
    Serial.write(receive[0]);
    Serial.write("\n");
    Serial.write("yo dawg2\n");
    i = 0;
  }

  if (digitalRead(button) == HIGH) {
    Serial.write("Hello World\n");
    delay(150);
  }
}
