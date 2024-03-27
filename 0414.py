# 0414.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 크기 조절하는 함수
dst = cv2.resize(src, dsize=(320, 240))
dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
