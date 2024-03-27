# 0501.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, 'data','Heart10.jpg')

src = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 

# src = cv2.imread('/data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

# 임계값을 수정하여 넣는 함수 - (이미지, 임계값, 최대값, 함수)
ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
print('ret=', ret)
cv2.imshow('dst',  dst)

# 자동으로 임계값을 정해주는 함수
ret2, dst2 = cv2.threshold(src, 200, 255,
                             cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print('ret2=', ret2)
cv2.imshow('dst2',  dst2)

cv2.waitKey()    
cv2.destroyAllWindows()
