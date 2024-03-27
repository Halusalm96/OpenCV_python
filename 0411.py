# 0411.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path) 
# img = cv2.imread(img_path) 

# src = cv2.imread('./data/lena.jpg')

# 채널 분리하는 함수
dst = cv2.split(src) 
print(type(dst))
print(type(dst[0])) # type(dst[1]), type(dst[2])

# 컬러지만 3개로 나누어 보임
cv2.imshow('blue',  dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red',   dst[2])
cv2.waitKey()    
cv2.destroyAllWindows()
