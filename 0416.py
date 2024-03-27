# 0416.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path) 

# src = cv2.imread('./data/lena.jpg')

# shape 값 나누기
rows, cols, channels = src.shape
# 이미지를 회전시키기 위한 변환 매트릭스 - (중심 좌표, 각도, 크기)
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 )
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )
# 매트릭스에 따라 변현시키는 함수 - (이미지, 매트릭스, 크기)
dst1 = cv2.warpAffine( src, M1, (rows, cols))
dst2 = cv2.warpAffine( src, M2, (rows, cols))

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
