#0306.py
import cv2
import numpy as np

# 이미지 사이즈 및 색깔
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# 이미지 중심 좌표
ptCenter = img.shape[1]//2, img.shape[0]//2
# 사이즈
size = 200,100

# 타원 그리기 - (이미지, 중심, 사이즈, 화전각도, 시작각도, 종료각도, 색)
cv2.ellipse(img, ptCenter, size, 0, 0, 360, (255, 0, 0))
# 외접하는 다각형 그리기 - (중신, 사이즈, 회전, 시작, 종료, 점의 각도)
pts1 = cv2.ellipse2Poly(ptCenter, size,  0, 0, 360, delta=45)

cv2.ellipse(img, ptCenter, size, 45, 0, 360, (255, 0, 0))
pts2 = cv2.ellipse2Poly(ptCenter, size, 45, 0, 360, delta=45)

cv2.polylines(img, [pts1, pts2], isClosed=True, color=(0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
