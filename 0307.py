#0307.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

x, y = 256, 256
size = 200

# 도형 각도 회전
for angle in range(0, 90, 10):
    # 직사각형 그리기
    rect = ((256, 256), (size, size), angle)
    box = cv2.boxPoints(rect).astype(np.int32)
    # random 랜덤 각도
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    cv2.polylines(img, [box], True, (b, g, r), 2)
    
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
