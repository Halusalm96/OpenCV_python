# 0405.py
import cv2
##import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

img = cv2.imread(img_path)

# img = cv2.imread('./data/lena.jpg')

##for y in range(100, 400):
##    for x in range(200, 300):
##        img[y, x, 0] = 255      
# 화면의 색을 구분하여 넣는 작업
# (세로)
img[100:400, 200:300, 0] = 255 
img[100:400, 300:400, 1] = 255
img[100:400, 400:500, 2] = 255
# (가로)
img[200:300, 100:400, 0] = 255 
img[300:400, 100:400, 1] = 255
img[400:500, 100:400, 2] = 255

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
