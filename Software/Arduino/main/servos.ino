void move() {
  int x_start = received_command[0];
  int y_start = received_command[1];
  int piece_type = received_command[2];
  int x_end = received_command[3];
  int y_end = received_command[4];
  int piece_captured = received_command[5];
  int captured_type = received_command[6];

  //if piece_captured == 1:
  
  //move x and y by x_end and y_end
  //move z by captured_type
  /////activate_electromagnet(true);
  //move z by -captured_type
  //move x by captured_x
  //move y by captured_y
  /////captured_y += 15;
  //move z by captured_type
  /////activate_electromagnet(false);
  //move z by -captured_type
  //move x and y by -x_end and -y_end
  
  move_x(x_start); //move x and y by x_start and y_start
  move_y(y_start);
  delay(3000);
  //move z by piece_type
  //activate_electromagnet(true);
  //move z by -piece_type
  move_x(x_end - x_start); //move x and y by (x_end-x_start) and (y_end-y_start)
  move_y(y_end - y_start);
  delay(3000);
  //move z by piece_type
  //activate_electromagnet(false);
  //move z by -piece_type
  move_x(-x_end);//move x and y by -x_end and -y_end
  move_x(-y_end);
}

void activate_electromagnet(boolean on) {
  if (on) {
    digitalWrite(electromagnet, HIGH);
  } else {
    digitalWrite(electromagnet, LOW);
  }
}

void move_x(int amount) {
  digitalWrite(X_ENABLE_PIN    , LOW);
  digitalWrite(Y_ENABLE_PIN    , LOW);

  int start = millis();
  while (millis() - start < abs(amount)) {
    if (amount > 0) {
      digitalWrite(X_DIR_PIN    , HIGH);
      digitalWrite(Y_DIR_PIN    , HIGH);
    } else {
      digitalWrite(X_DIR_PIN    , LOW);
      digitalWrite(Y_DIR_PIN    , LOW);
    }
    move_help();
  }

  digitalWrite(X_ENABLE_PIN    , HIGH);
  digitalWrite(Y_ENABLE_PIN    , HIGH);
}

void move_y(int amount) {
  digitalWrite(E_ENABLE_PIN    , LOW);
  digitalWrite(Q_ENABLE_PIN    , LOW);

  int start = millis();
  while (millis() - start < abs(amount)) {
    if (amount > 0) {
      digitalWrite(E_DIR_PIN    , HIGH);
      digitalWrite(Q_DIR_PIN    , HIGH);
    } else {
      digitalWrite(E_DIR_PIN    , LOW);
      digitalWrite(Q_DIR_PIN    , LOW);
    }
    move_help();
  }

  digitalWrite(E_ENABLE_PIN    , HIGH);
  digitalWrite(Q_ENABLE_PIN    , HIGH);
}

void move_z(int amount) {
  delay(50);
  digitalWrite(Z_ENABLE_PIN    , LOW);

  int start = millis();
  while (millis() - start < abs(amount)) {
    if (amount > 0) {
      digitalWrite(Z_DIR_PIN    , HIGH);
    } else {
      digitalWrite(Z_DIR_PIN    , LOW);
          }
    move_help();
  }
  digitalWrite(Z_ENABLE_PIN    , HIGH);
  delay(50);
}

void move_help() {
  digitalWrite(X_STEP_PIN    , HIGH);
  digitalWrite(Y_STEP_PIN    , HIGH);
  digitalWrite(Z_STEP_PIN    , HIGH);
  digitalWrite(E_STEP_PIN    , HIGH);
  digitalWrite(Q_STEP_PIN    , HIGH);
  delay(.01);
  digitalWrite(X_STEP_PIN    , LOW);
  digitalWrite(Y_STEP_PIN    , LOW);
  digitalWrite(Z_STEP_PIN    , LOW);
  digitalWrite(E_STEP_PIN    , LOW);
  digitalWrite(Q_STEP_PIN    , LOW);
}


