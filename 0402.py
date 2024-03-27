# 0402.py
import cv2
##import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 
# img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# 차원의 자세한 정보 확인 (2차원 - 흑백)
print('img.shape=', img.shape)

##img = img.reshape(img.shape[0]*img.shape[1])
# shape 안에 있는 정수 전부 곱하기
img = img.flatten()
print('img.shape=', img.shape)

# shape 정수 재배치 (-1은 거의 자동으로 배치해줌)
img = img.reshape(-1, 512, 512)
print('img.shape=', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()
