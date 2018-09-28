from compute_board import state_tracker
from process_images import detect,transform_board,get_snapshot
import scipy.misc
import cv2
import numpy as np
import chess.uci
import serial
import sys



#Assume player is white

# m, img = detect()
# np.save("m.npy", m)
# print("chessboard detected")
# t_img = transform_board(m, img)
# cv2.imshow("image", t_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###
m = np.load("m.npy")
state_tracker = state_tracker("cnn.h5",m)
img = get_snapshot() #gets current image of board
new_state = state_tracker.compute_new_state(img,rotate=1,flip=1) #Need to change depending on orientation

print(new_state)
print(state_tracker.conv_to_state(state_tracker.board))
np.testing.assert_array_equal(new_state,state_tracker.conv_to_state(state_tracker.board))
engine = chess.uci.popen_engine("stockfish_8_x64.exe")
engine.uci()
print(engine.name)

ser = serial.Serial("COM3", 9600)
while(not state_tracker.board.is_checkmate()):
    #wait for button press
    move = input("Press Enter to continue...")
    img = get_snapshot()
    new_state = state_tracker.compute_new_state(img,rotate=1,flip=1) #Need to change depending on orientation
    print("current state")
    print(state_tracker.state)
    print("computed state")
    print(new_state)
    playermove = state_tracker.compute_move(new_state)
    #playermove = chess.Move(state_tracker.conversion.index(move[0].upper()+move[1]),state_tracker.conversion.index(move[2].upper()+move[3]))
    print("Player M move")
    print(playermove.uci())
    state_tracker.make_move(playermove)
    print(state_tracker.conv_to_state(state_tracker.board))
    engine.position(state_tracker.board)
    (bestmove, ponder) = engine.go(movetime=100)
    print("Stock Makes Move:")
    print(bestmove.uci())
    y_start = bestmove.uci()[0].upper()
    x_start = str(int(bestmove.uci()[1]))
    piece_start = str(state_tracker.piece_number.index(state_tracker.board.piece_at(state_tracker.conversion.index("" + y_start + x_start)).symbol().upper()))
    y_end = bestmove.uci()[2].upper()
    x_end = str(bestmove.uci()[3])
    print()
    piece_end = state_tracker.board.piece_at(state_tracker.conversion.index("" + y_end + x_end))
    if None != piece_end:
        piece_captured = "1"
        captured_type = str(state_tracker.piece_number.index(piece_end.symbol().upper()))
    else:
        piece_captured = "0"
        captured_type = "0"
    send_arr = x_start+y_start+piece_start+x_end+y_end+piece_captured+captured_type
    print(send_arr)
    ser.write(str.encode(send_arr,"ascii"))
    res = ser.read(size=7)
    print("arduino sent back "+ res.decode())
    #output bestmove to arduino
    state_tracker.make_move(bestmove)
    print(state_tracker.state)
