import numpy as np
import cv2
from scipy.spatial.distance import euclidean
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from itertools import product
image = cv2.imread('chess_board5.jpg')
#image[:,:,0] = 0
#image[:,:,1] = 0
equ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#equ = cv2.bitwise_not(equ)
#ret,equ = cv2.threshold(equ, 130 ,255,cv2.THRESH_BINARY)
# cv2.imshow('same',equ)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
board_size = (7,7)
found, corners = cv2.findChessboardCorners(equ, board_size, flags=cv2.CALIB_CB_ADAPTIVE_THRESH)
print(found)
img = cv2.drawChessboardCorners(equ, board_size, corners, found)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(corners.shape)
assert found, "Couldn't find chessboard."

z = corners.reshape((49, 2))
board_center = z[24]
frame_center = image.shape[1] / 2.0, image.shape[0] / 2.0

assert euclidean(board_center, frame_center) < 20.0, "Camera is not centered over chessboard."

X_train = np.array(list(product(np.linspace(3, -3, 7), np.linspace(-3, 3, 7))))
print(X_train)
poly = PolynomialFeatures(degree=4)
X_train = poly.fit_transform(X_train)
z_x = z[:,0]
m_x = LinearRegression()
m_x.fit(X_train, z_x)
z_y = z[:,1]
m_y = LinearRegression()
m_y.fit(X_train, z_y)
print(z[:,0][::-1])
print(z[:,1])
print(z[0,:])
def predict(i, j):
    features = poly.fit_transform(np.array([[i, j]]))
    return m_x.predict(features), m_y.predict(features)


P = []
Q = []

P.append(predict(-4.0, -4.0))
Q.append((0.0, 0.0))

P.append(predict(-4.0, 4.0))
Q.append((0.0, 480.0))

P.append(predict(4.0, -4.0))
Q.append((480.0, 0.0))

P.append(predict(4.0, 4.0))
Q.append((480.0, 480.0))
print(predict(4.0,4.0))
cv2.circle(image,predict(-4.0,-4.0),1,(255,0,0))
cv2.circle(image,(z_x[0],z_y[0]),1,(255,0,0))
cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(P)
print(Q)
Q = np.array(Q, np.float32)
P = np.array(P, np.float32).reshape(Q.shape)
print(P)
print(Q)
M = cv2.getPerspectiveTransform(P, Q)
bgr_img = cv2.warpPerspective(image, M, (480,480))
print(bgr_img.shape)
cv2.imshow('bgr_img',bgr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# image = cv2.imread('chess_board3.jpg')
# image[:,:,0] = 0
# image[:,:,1] = 0
# equ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# equ = cv2.bitwise_not(equ)
# equ = cv2.equalizeHist(equ)
#
# cv2.imshow('preprocess',equ)
# ret, thresh = cv2.threshold(equ,115,255,cv2.THRESH_BINARY)
# cv2.imshow('thress',thresh)
#
# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# im2 = cv2.drawContours(image, contours, -1, (0,255,0), 3)
# cv2.imshow('Corners',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()