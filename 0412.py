# 0412.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path) 

# src = cv2.imread('./data/lena.jpg')

# 채널 분리하는 함수 (3개의 값으로 분리)
b, g, r = cv2.split(src)
# 채널 병합 (분리된 채널 병합)
dst = cv2.merge([b, g, r]) 

print(type(dst))
print(dst.shape)
cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
