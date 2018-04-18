boolean moveMade() {
  return (digitalRead(button) == HIGH);
}

void computerTurn() {
  Serial.write("Player Made Move");
}

void playerTurn() {
  
}

void receiveCommand() {
  while (Serial.available() <= 0) {
    //wait for command to become available
  }
  i = 0;
  while (Serial.available() > 0) {    // if data present, blink
    received_command[i] = Serial.read();
    i++;
    digitalWrite(LED, HIGH);
    delay(100);
    digitalWrite(LED, LOW);
    delay(100);
  }
}

