import numpy as np
import cv2
import os
from scipy.spatial.distance import euclidean
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from itertools import product


def detect_chessboard(image):
    equ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    board_size = (7, 7)
    found, corners = cv2.findChessboardCorners(equ, board_size, flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
    return found,equ


def create_transform(image):
    #image = cv2.imread(img_path)
    equ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    board_size = (7, 7)
    found, corners = cv2.findChessboardCorners(equ, board_size, flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
    assert found, "Couldn't find chessboard."
    '''
    Draws and shows the corners found
    img = cv2.drawChessboardCorners(equ, board_size, corners, found)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(corners.shape)
    '''
    z = corners.reshape((49, 2))
    board_center = z[24]
    frame_center = image.shape[1] / 2.0, image.shape[0] / 2.0
    assert euclidean(board_center, frame_center) < 20.0, "Camera is not centered over chessboard."

    x_train = np.array(list(product(np.linspace(3, -3, 7), np.linspace(-3, 3, 7))))
    poly = PolynomialFeatures(degree=4)
    x_train = poly.fit_transform(x_train)
    z_x = z[:, 0]
    m_x = LinearRegression()
    m_x.fit(x_train, z_x)
    z_y = z[:, 1]
    m_y = LinearRegression()
    m_y.fit(x_train, z_y)

    def predict(i, j):
        features = poly.fit_transform(np.array([[i, j]]))
        return m_x.predict(features), m_y.predict(features)

    p = []
    q = []

    p.append(predict(-4.0, -4.0))
    q.append((0.0, 0.0))

    p.append(predict(-4.0, 4.0))
    q.append((0.0, 480.0))

    p.append(predict(4.0, -4.0))
    q.append((480.0, 0.0))

    p.append(predict(4.0, 4.0))
    q.append((480.0, 480.0))

    cv2.circle(image, predict(-4.0, -4.0), 1, (255, 0, 0))
    cv2.circle(image, (z_x[0], z_y[0]), 1, (255, 0, 0))
    '''
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    q = np.array(q, np.float32)
    p = np.array(p, np.float32).reshape(q.shape)

    m = cv2.getPerspectiveTransform(p, q)
    # np.save('transform.npy', m)
    return m


def get_snapshot():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    return frame


def detect():
    cap = cv2.VideoCapture(1)
    found = False
    image = None
    while not found:
        # Capture frame-by-frame
        ret, frame = cap.read()
        found, gray = detect_chessboard(frame)
        # Our operations on the frame come here
        if found:
            image = frame
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print("found")
    m = create_transform(image)
    return m,image


def split_board(image,img_path):
    square_size = int(image.shape[0]/8)
    squares_folder = os.path.join(img_path,'squares')
    if not os.path.exists(squares_folder):
        os.mkdir(squares_folder)
    for i in range(8):
        for j in range(8):
            square = image[square_size*i:square_size*(i+1),square_size*j:square_size*(j+1)]
            write_path = os.path.join(squares_folder,str(i*8+j)+'.jpg')
            cv2.imwrite(write_path, square)


def transform_board(m,image):
    img = cv2.warpPerspective(image, m, (480,480))
    return img


if __name__ == "__main__":
    raw_path = os.path.join('../raw_data')
    processed_path = os.path.join('../processed_data')
    assert os.path.exists(raw_path), 'No raw data or raw data in wrong directory'
    if not os.path.exists(processed_path):
        os.mkdir(processed_path)
    empty_board = cv2.imread('test.jpg')
    transform_mat = create_transform(empty_board)
    #np.save("m.npy",transform_mat)
    # for i in os.listdir(raw_path):
    #     if 'empty' not in i:
    #         img_path = os.path.join(processed_path, i.split('.')[0])
    #         if not os.path.exists(img_path):
    #             os.mkdir(img_path)
    #         chess_board = cv2.imread(os.path.join(raw_path, i))
    #         chess_board = transform_board(transform_mat,chess_board)
    #         split_board(chess_board, img_path)
