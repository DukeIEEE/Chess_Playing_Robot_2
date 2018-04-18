#include "defines.h"

int LED = 4;      // LED connected to digital pin 4
int electromagnet = 3;
int button = 2;
int x;
int i = 0;
int received_command[10]; //
boolean player_turn;

void setup() {
   pinMode(X_STEP_PIN  , OUTPUT);
   pinMode(X_DIR_PIN    , OUTPUT);
   pinMode(X_ENABLE_PIN    , OUTPUT);
  
   pinMode(Y_STEP_PIN  , OUTPUT);
   pinMode(Y_DIR_PIN    , OUTPUT);
   pinMode(Y_ENABLE_PIN    , OUTPUT);
    
   pinMode(Z_STEP_PIN  , OUTPUT);
   pinMode(Z_DIR_PIN    , OUTPUT);
   pinMode(Z_ENABLE_PIN    , OUTPUT);

  
   Serial.begin(9600);
   pinMode(LED, OUTPUT);
   pinMode(electromagnet, OUTPUT);    
   pinMode(button, INPUT);
}

void loop() {
  if (player_turn && moveMade()) { //Signal for computer to do its magic
    player_turn = false;
    computerTurn(); //Tells computer that player finished turn
    receiveCommand(); //Fetch command from computer
    move(); //move piece from one position to another
    player_turn = true;
    
  } else {
    playerTurn(); //Does nothing. Could potentially add timer functionality
  }
}
