# 0404.py
import cv2
##import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

img = cv2.imread(img_path)

# img = cv2.imread('./data/lena.jpg') # cv2.IMREAD_COLOR
img[100, 200] = [255, 0, 0]  # 컬러(BGR) 변경
print(img[100, 200:210]) # ROI 접근

##for y in range(100, 400):
##    for x in range(200, 300):
##        img[y, x] = [255, 0, 0]    # 파랑색(blue)으로 변경

img[100:400, 200:300] = [255, 0, 0]  # ROI 접근
    
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
