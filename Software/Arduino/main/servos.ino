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
    activate_electromagnet(true);
    //move z by -captured_type
    //move x by captured_x
    //move y by captured_y
    captured_y += 15;
    //move z by captured_type
    activate_electromagnet(false);
    //move z by -captured_type
    //move x and y by -x_end and -y_end
    
  //move x and y by x_start and y_start
  //move z by piece_type
  activate_electromagnet(true);
  //move z by -piece_type
  //move x and y by (x_end-x_start) and (y_end-y_start)
  //move z by piece_type
  activate_electromagnet(false);
  //move z by -piece_type
  //move x and y by -x_end and -y_end
}

void activate_electromagnet(boolean on) {
  if (on) {
    digitalWrite(electromagnet, HIGH);
  } else {
    digitalWrite(electromagnet, LOW);
  }
}

void move_x(int amount) {
  
}

void move_y(int amount) {
  
}

void move_z(int amount) {
  
}


