//Servos
#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62

#define E_STEP_PIN         26
#define E_DIR_PIN          28
#define E_ENABLE_PIN       24

#define Q_STEP_PIN         36
#define Q_DIR_PIN          34
#define Q_ENABLE_PIN       30

#define SDPOWER            -1
#define SDSS               53
#define LED_PIN            13
#define PS_ON_PIN          12
#define KILL_PIN           -1



enum PIECE_TYPE {
    KING_T = 0,
    QUEEN_T = 1,
    ROOK_T = 2,
    BISHOP_T = 3,
    KNIGHT_T = 4,
    PAWN_T = 5
};

enum PIECE_HEIGHTS {
    K_H = 500,
    Q_H = 500,
    R_H = 500,
    B_H = 500,
    N_H = 500,
    P_H = 2800
};

const int sqy = 330;
const int sqx = 260;

enum Y_POSITIONS {
    A = 260,
    B = A + sqy,
    C = B + sqy,
    D = C + sqy,
    E = D + sqy,
    F = E + sqy,
    G = F + sqy,
    H = G + sqy,
};

enum X_POSITIONS {
    ONE = 260,
    TWO = ONE     + sqx,
    THREE = TWO   + sqx,
    FOUR = THREE  + sqx,
    FIVE = FOUR   + sqx,
    SIX = FIVE    + sqx,
    SEVEN = SIX   + sqx,
    EIGHT = SEVEN + sqx,
};

int captured_x = 220;
int captured_y = 100;

