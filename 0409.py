# 0409.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path,  cv2.IMREAD_GRAYSCALE) 

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

##dst = src
# 영상 복사          
dst = src.copy()
dst[100:400, 200:300] = 0

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
