void move() {
//  char x_start_c = received_command[0];
//  char y_start_c = received_command[1];
//  char piece_type_c = received_command[2];
//  char x_end_c = received_command[3];
//  char y_end_c = received_command[4];
//  char piece_captured_c = received_command[5];
//  char captured_type_c = received_command[6];

  char x_start_c = command.charAt(0);
  char y_start_c = command.charAt(1);
  char piece_type_c = command.charAt(2);
  char x_end_c = command.charAt(3);
  char y_end_c = command.charAt(4);
  char piece_captured_c = command.charAt(5);
  char captured_type_c = command.charAt(6);

  int x_start;
  int y_start;
  int piece_type;
  int x_end;
  int y_end;
  int piece_captured;
  int captured_type;

  x_start = X_array[x_start_c - '0'];
  y_start = Y_array[(int)y_start_c - 64];

  for (int k = 0; k < command.length() ; k++) {
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
  }
  command = "";
//  for (int k = 0; k < (y_start_c - 64); k++) {
//    digitalWrite(LED, HIGH);
//    delay(200);
//    digitalWrite(LED, LOW);
//    delay(200);
//  }

  x_end = X_array[x_end_c - '0'];
  y_end = Y_array[(int)y_end_c - 64];

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
  delay(1000);
  //move z by piece_type
  //activate_electromagnet(true);
  //move z by -piece_type
  move_x(x_end - x_start); //move x and y by (x_end-x_start) and (y_end-y_start)
  move_y(y_end - y_start);
  delay(1000);
  //move z by piece_type
  //activate_electromagnet(false);
  //move z by -piece_type
  move_x(-x_end);//move x and y by -x_end and -y_end
   move_y(-y_end);

   software_Reset();
}

void activate_electromagnet(boolean on) {
  if (on) {
    digitalWrite(electromagnet, HIGH);
  } else {
    digitalWrite(electromagnet, LOW);
  }
}

void move_x(int amount) {
      delay(10);
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
      delay(10);
}

void move_y(int amount) {
    delay(10);
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
      delay(10);
}

void move_z(int amount) {
  delay(10);
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
  delay(10);
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


