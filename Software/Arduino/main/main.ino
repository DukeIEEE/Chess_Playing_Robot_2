#include "defines.h"

int LED = 43;      // LED connected to digital pin 4
int electromagnet = 32;
int button = 45;
int start;
int i = 0;
int j;
char received_command[7]; //
String command;
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

  pinMode(E_STEP_PIN  , OUTPUT);
  pinMode(E_DIR_PIN    , OUTPUT);
  pinMode(E_ENABLE_PIN    , OUTPUT);

  pinMode(Q_STEP_PIN  , OUTPUT);
  pinMode(Q_DIR_PIN    , OUTPUT);
  pinMode(Q_ENABLE_PIN    , OUTPUT);

  digitalWrite(X_ENABLE_PIN    , HIGH);
  digitalWrite(Y_ENABLE_PIN    , HIGH);
  digitalWrite(Z_ENABLE_PIN    , HIGH);
  digitalWrite(E_ENABLE_PIN    , HIGH);
  digitalWrite(Q_ENABLE_PIN    , HIGH);

  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(electromagnet, OUTPUT);
  pinMode(button, INPUT);

  //move_x(5000);
  start = millis();
}

void software_Reset() // Restarts program from beginning but does not reset the peripherals and registers
{
asm volatile ("  jmp 0");  
}  

void loop() {
  //if (player_turn && moveMade()) { //Wait for physical button press
  //if (player_turn == false) {
  //  player_turn = true;
  receiveCommand(); //Fetch command from computer
  move(); //move piece from one position to another
  //  player_turn = true;
}

