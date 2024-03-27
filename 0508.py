# 0508.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, 'data', 'fruits.jpg')

src = cv2.imread(img_path)

#1
# src = cv2.imread('./data/fruits.jpg')
# 컬러를 나타내는 BGR 함수
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# 이미지를 각 채널로 분리하는 함수
h, s, v = cv2.split(hsv)

#2
# roi 관심 영역으로 선택한 함수
roi = cv2.selectROI(src)
print('roi =', roi)
roi_h = h[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
# 히스토그램 계산하는 함수
hist = cv2.calcHist([roi_h], [0], None,[64], [0, 256])
# 역투영 하는 함수
backP= cv2.calcBackProject([h.astype(np.float32)], [0], hist,[0, 256],scale=1.0)
##minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(backP)
##T = maxVal -1 # threshold

#3
hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)
k = 1 
T = hist[k][0] -1 # threshold
print('T =', T)
ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)

cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
