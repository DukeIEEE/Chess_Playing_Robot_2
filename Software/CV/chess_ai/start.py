from compute_board import state_tracker
from process_images import detect,transform_board,get_snapshot
import scipy.misc
import cv2
import numpy as np
import chess.uci
import sys



#Assume player is white

#m,img = detect()
#np.save("m.npy",m)
#print("chessboard detected")
#t_img = transform_board(m,img)
#cv2.imshow("image",t_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
m = np.load("m.npy")
state_tracker = state_tracker("cnn.h5",m)
img = get_snapshot() #gets current image of board
new_state = state_tracker.compute_new_state(img,rotate=0,flip=1) #i don't think we need to rotate image, but we will see

print(new_state)
print(state_tracker.conv_to_state(state_tracker.board))
np.testing.assert_array_equal(new_state,state_tracker.conv_to_state(state_tracker.board))
engine = chess.uci.popen_engine("stockfish_8_x64.exe")
engine.uci()
print(engine.name)
while(not state_tracker.board.is_checkmate()):
    #wait for button press
    input("Press Enter to continue...")
    img = get_snapshot()
    new_state = state_tracker.compute_new_state(img,rotate=0,flip=1)
    print("current state")
    print(state_tracker.state)
    print("computed state")
    print(new_state)
    playermove = state_tracker.compute_move(new_state)
    print("player move")
    print(playermove.uci())
    state_tracker.make_move(playermove)
    print(state_tracker.conv_to_state(state_tracker.board))
    engine.position(state_tracker.board)
    (bestmove, ponder) = engine.go(movetime=100)
    print("robot move")
    print(bestmove.uci())
    x_start = bestmove.uci()[0].toUpper()
    y_start = bestmove.uci()[1]
    lan = state_tracker.board.lan(bestmove)
    if lan[0].isLower():
        piece_type = 5
    elif lan[0] == "N":
        piece_type = 4
    elif lan[0] == "B":
        piece_type = 3
    elif lan[0] == "R":
        piece_type = 2
    elif lan[0] == "Q":
        piece_type = 1
    elif lan[0] == "K":
        piece_type = 0
    x_end = bestmove.uci()[2].toUpper()
    y_end = bestmove.uci()[3]
    if "x" in lan:
        piece_captured = 1
        piece = state_tracker.board.piece_at(state_tracker.conversion.index(""+x_end+y_end))
        if piece.symbol() == "P":
            captured_type = 5
        elif piece.symbol() == "N":
            captured_type = 4
        elif piece.symbol() == "B":
            captured_type = 3
        elif piece.symbol() == "R":
            captured_type = 2
        elif piece.symbol() == "Q":
            captured_type = 1
        elif piece.symbol() == "K":
            captured_type = 0
    else:
        piece_captured = 0
        captured_type = 0
    #output bestmove to arduino
    state_tracker.make_move(bestmove)
    print(state_tracker.state)