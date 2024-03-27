# 0410.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path,  cv2.IMREAD_GRAYSCALE) 
 
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# 컬러로 바꾸는 과정
shape = src.shape[0], src.shape[1], 3
dst1 = np.zeros(shape, dtype=np.uint8)
dst2 = np.zeros(shape, dtype=np.uint8)
dst3 = np.zeros(shape, dtype=np.uint8)

# 색을 정하는 함수
dst1[:,:,0] = src  
dst2[:,:,1] = src 
dst3[:,:,2] = src

dst1[100:300, 200:400, :] = [255, 255, 255]
dst2[100:200, 200:250, :] = [255, 255, 255]
dst3[100:500, 100:300, :] = [255, 255, 255]

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()    
cv2.destroyAllWindows()
