import chess
import numpy as np
import cv2
import scipy.misc
from keras.models import load_model
class state_tracker():
    def __init__(self,model_path,m):
        # [1,0,0] is white, [0,1,0] is black, [0,0,1] is empty in pred
        # white is 1, black is 0 in state
        self.classifier = load_model(model_path)
        self.board = chess.Board()
        self.board.push
        self.state = self.conv_to_state()
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
        return board_state

    def make_move(self,move):
        #self.board.push_san(move)
        self.board.push(move)
        self.state = self.conv_to_state()
        self.turn = not self.turn

    def compute_move(self,new_state,promotion=None):
        diff = self.state-new_state
        print(diff)
        if self.turn == chess.WHITE:
            print(np.where(diff==2))
            from_ind = np.where(diff==2)[0][0]*8+np.where(diff==2)[1][0]
            to_ind = np.where(diff==-2)[0][0]*8+np.where(diff==-2)[1][0]
        else:
            from_ind = np.where(diff == 1)[0][0] * 8 + np.where(diff == 1)[1][0]
            to_ind = np.where(diff == -1)[0][0] * 8 + np.where(diff == -1)[1][0]
        self.state = new_state
        move = chess.Move(from_ind,to_ind) #eventually introduce promotion
        return move

    def compute_new_state(self, img):
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
                print(pred)
                pred_value = np.argmax(pred)
                if pred_value == 0:
                    state[i,j] = 1
                if pred_value == 1:
                    state[i,j] = 0
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
