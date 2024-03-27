#0303.py
import cv2
import numpy as np

# 이미지 사이즈 및 색상
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# 이미지 위치 좌표 (256,256)
cy = img.shape[0]//2 #256
cx = img.shape[1]//2 #256

# 원 그리기 (2개 그리기)
for r in range(200, 0, -100):
    # 원그리기 - (이미지, 중심, 반지름, 선색)
    cv2.circle(img, (cx, cy), r, color=(255, 0, 0))

# 원그리기 - (이미지, 중심, 반지름, 선색, 채우기)
cv2.circle(img, (cx, cy), radius=50, color=(0, 0, 255), thickness=-1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
