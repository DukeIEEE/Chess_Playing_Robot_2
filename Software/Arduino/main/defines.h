//Servos

#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

enum PIECE_HEIGHTS {
    KING = 41,
    QUEEN = 34,
    ROOK = 20,
    BISHOP = 28,
    KNIGHT = 24,
    PAWN = 19
};

enum X_POSITIONS {
    A = 100,
    B = 115,
    C = 130,
    D = 145,
    E = 160,
    F = 175,
    G = 190,
    H = 205,
};

enum Y_POSITIONS {
    ONE = 100,
    TWO = 115,
    THREE = 130,
    FOUR = 145,
    FIVE = 160,
    SIX = 175,
    SEVEN = 190,
    EIGHT = 205,
};

int captured_x = 220;
int captured_y = 100;

