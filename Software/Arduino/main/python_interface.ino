boolean moveMade() {
  return (digitalRead(button) == HIGH);
}

void computerTurn() {

}

void playerTurn() {

}

void receiveCommand() {
  int start = 0;
  while (Serial.available() <= 0) {
    //wait for command to become available
    delay(10);
    if (millis() - start > 10000) {
      software_Reset();
    }
  }
  i = 0;
  while (Serial.available() > 0) {    // if data present, blink
   //received_command[i++] = Serial.read();
   command = Serial.readString();
   // digitalWrite(LED, HIGH);
    delay(10);
//    digitalWrite(LED, LOW);
//    delay(5);
  }
      Serial.write(command[0]);
      Serial.write(command[1]);
      Serial.write(command[2]);
      Serial.write(command[3]);
      Serial.write(command[4]);
      Serial.write(command[5]);
      Serial.write(command[6]);
      Serial.flush();
}

