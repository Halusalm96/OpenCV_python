# 0404_1.py
import cv2
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img_path1 = os.path.join(current_dir, './data/man_face.jpg')
img_path2 = os.path.join(current_dir, './data/skull.jpg')

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)

dst1 = np.zeros(img1.shape, dtype=img1.dtype)
dst2 = np.zeros(img2.shape, dtype=img2.dtype)

N=2
h1 , w1, r1 = img1.shape
h2 , w2, r2 = img2.shape

img1[:h1, :w1//2 ,:] = [0, 0, 0]
img2[:, w2//2:, :] = [0, 0, 0]

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)

dst1 = img1 + img2
dst2 = cv2.add (img1,img2)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)

b,g,_=dst2.shape

h = b // 2

print(h,g)

for i in range(h-20, h+20):
    for j in range(g):
        x = i*h
        y = j*g
        roi = dst2[x:x+h , y:y+g]
        dst2[x:x+h , y:y+g] = cv2.mean(roi)[0:3]

cv2.waitKey()
cv2.destroyAllWindows()
