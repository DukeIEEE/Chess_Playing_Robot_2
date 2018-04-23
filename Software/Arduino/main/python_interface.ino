boolean moveMade() {
  return (digitalRead(button) == HIGH);
}

void computerTurn() {

}

void playerTurn() {

}

void receiveCommand() {
  
  while (Serial.available() <= 0) {
    //wait for command to become available
  }
  i = 0;
  while (Serial.available() > 0) {    // if data present, blink
   //received_command[i++] = Serial.read();
   command = Serial.readString();
   // digitalWrite(LED, HIGH);
    delay(1);
//    digitalWrite(LED, LOW);
//    delay(1);
  }
}

