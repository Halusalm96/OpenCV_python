# 0406.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, dtype=src.dtype)

# 화면을 몇개로 나눌지 정하는 변수
N = 4 # 8, 32, 64
# 2차원임으로 X축과 Y축을 변수로 지정
height, width = src.shape
##height, width, channel = src.shape

# X축과 Y축을 나워 부분을 정하는 함수
h = height // N
w = width  // N
# N = 4임으로 0,1,2,3이 반복됨
for i in range(N):
    for j in range(N):
        # 나눠진 N개를 채우는 함수
        y = i*h #i * height / N > i는 N까지 오는 현상
        x = j*w #j * width / N > j는 N까지 오는 현상     
        roi = src[y:y+h, x:x+w] #나눠진 곳을 비슷한 색으로 칠하는 함수
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0]
##        dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3]
        
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
