# 0516.py
import cv2
import numpy as np 
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, 'data', 'tsukuba_l.png')

# 흑백
src = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

#1
# src = cv2.imread('./data/tsukuba_l.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

#2
# 히스토그램 평활화
dst = cv2.equalizeHist(src)
cv2.imshow('dst', dst)

#3
# 함수의 한계를 지정하고 지정한 크기에 따라 이미지를 분활하는 함수
clahe2 = cv2.createCLAHE(clipLimit=40, tileGridSize=(1,1))
dst2 = clahe2.apply(src)
cv2.imshow('dst2', dst2)

#4
clahe3 = cv2.createCLAHE(clipLimit=40, tileGridSize=(8,8))
dst3 = clahe3.apply(src)
cv2.imshow('dst3', dst3)

cv2.waitKey()    
cv2.destroyAllWindows()
