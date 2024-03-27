#0301.py
import cv2
import numpy as np

# 이미지 사이즈 및 색상 - (사이즈, 타입) + 색상(0-검 / 255-흰)
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# 다른게 표현할 수 있는 함수
#img = np.ones((512,512,3), np.uint8) * 255
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#img = np.zeros((512,512, 3), np.uint8) # Black 배경
# 점의 위치
pt1 = 100, 100
pt2 = 400, 400
# 직사각형 그리기 - (이미지, 점, 점, 색, 두께)
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

# 직선 그리기 - (이미지, 점, 점 ,색, 두께)
cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
