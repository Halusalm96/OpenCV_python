# 0413.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path) 

# src = cv2.imread('./data/lena.jpg')

# 이미지의 컬러를 변화하는 함수
gray   = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# bgr1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
hsv    = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
bgr2   = cv2.cvtColor(src, cv2.COLOR_HSV2BGR)
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
bgr3    = cv2.cvtColor(src, cv2.COLOR_YCrCb2BGR)

cv2.imshow('gray',  gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv',   hsv)
# cv2.imshow('bgr1', bgr1)
cv2.imshow('bgr2', bgr2)
cv2.imshow('bgr3', bgr3)

cv2.waitKey()    
cv2.destroyAllWindows()
