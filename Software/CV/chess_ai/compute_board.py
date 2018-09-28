import chess
import numpy as np
import cv2
import scipy.misc
import sys
from keras.models import load_model


class state_tracker():
    def __init__(self,model_path,m):
        # [1,0,0] is white, [0,1,0] is black, [0,0,1] is empty in pred
        # white is 1, black is 0 in state
        self.classifier = load_model(model_path)
        self.board = chess.Board()
        self.board.push
        self.piece_number = ["K","Q","R","B","N","P"]
        self.conversion = ["A1","B1","C1","D1","E1","F1","G1","H1",
                           "A2","B2","C2","D2","E2","F2","G2","H2",
                           "A3","B3","C3","D3","E3","F3","G3","H3",
                           "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
                           "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
                           "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
                           "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
                           "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]
        self.state = self.conv_to_state()
        self.prev_state = self.conv_to_state()
        self.turn = chess.WHITE # white is true, black is false
        self.m = m
    def conv_to_state(self,board = None):
        if board == None:
            board_str = self.board.fen()
        else:
            board_str = board.fen()
        state = board_str.split(" ")[0]
        row_state = state.split("/")
        board_state = -1*np.ones((8,8))
        for i,row in enumerate(row_state):
            j=0
            for char in row:
                if char.isdigit():
                    j+= int(char)
                elif char.isupper():
                    board_state[i,j] = 1
                    j+=1
                elif char.islower():
                    board_state[i,j] = 0
                    j+=1
        board_state = np.flip(board_state, 1) #fen string starts with black side, need to flip to have array index match chess notation
        return board_state

    def make_move(self,move):
        self.board.push(move)
        self.prev_state = self.state
        self.state = self.conv_to_state()
        self.turn = not self.turn

    def compute_move(self,new_state,promotion=None): #only checks for white propertly
        diff = self.state-new_state
        diff = np.rot90(diff,2,(0,1))
        print("this is diff")
        print(diff)
        if self.turn == chess.WHITE:
            #check castling
            if len(np.where(diff==2)[0])==2:
                assert np.where(diff[0][0]==2) == 0
                if diff[0][0] == 2:
                    from_ind = 4
                    to_ind = 2
                elif diff[0][7] == 2:
                    from_ind = 4
                    to_ind = 6
                else:
                    assert False
            else:
                from_ind = np.where(diff==2)[0][0]*8+np.where(diff==2)[1][0]
                try:
                    to_ind = np.where(diff==-2)[0][0]*8+np.where(diff==-2)[1][0]
                except IndexError:
                    print("white took a piece")
                    to_ind = np.where(diff==-1)[0][0]*8+np.where(diff==-1)[1][0]
        else:
            from_ind = np.where(diff == 1)[0][0] * 8 + np.where(diff == 1)[1][0]
            to_ind = np.where(diff == -1)[0][0] * 8 + np.where(diff == -1)[1][0]
        self.state = new_state
        move = chess.Move(from_ind,to_ind) #eventually introduce promotion
        return move

    def compute_new_state(self, img,rotate=0,flip=0):
        image = cv2.warpPerspective(img, self.m, (480, 480))
        square_size = int(image.shape[0] / 8)
        state = -1*np.ones((8,8))
        for i in range(8):
            for j in range(8):
                square = image[square_size * i:square_size * (i + 1), square_size * j:square_size * (j + 1)]
                r, g, b = square[:, :, 0], square[:, :, 1], square[:, :, 2]
                gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
                gray = gray.astype('float32')
                gray /= 255
                pred = self.classifier.predict(gray.reshape(1,square_size,square_size,1))
                #print(pred)
                pred_value = np.argmax(pred)
                if pred_value == 0:
                    state[i,j] = 1
                if pred_value == 1:
                    state[i,j] = 0
        state = np.rot90(state,rotate,(0,1))
        if flip:
            state = np.flip(state,0)
        return state

def main():
    m = np.load("m.npy")
    state = state_tracker("cnn.h5",m)
    img = scipy.misc.imread("../raw_data/7.jpg")
    new_state = state.compute_new_state(img)
    print(new_state)
    #
    # state.make_move("e4")
    # board = chess.Board()
    # board.push_san("e4")
    # board.push_san("e5")
    # print(state.state)
    # print(state.conv_to_state(board))
    # print(state.compute_move(state.conv_to_state(board)))
    # print(chess.E2)
    # print(chess.E4)
    ...
if __name__ == "__main__":
    main()
