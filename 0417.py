# 0417.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 

# src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100

# 연산을 통해 픽셀의 값을 더하는 함수
dst1 = src1 + src2
# 함수를 통해 이미지를 더하는 함수 (255를 초과하는 경우 255로 클리핑)
dst2 = cv2.add(src1, src2)
#dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()
cv2.destroyAllWindows()
