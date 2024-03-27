#0305.py
import cv2
import numpy as np

# 이미지 사이즈 및 색상
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# 도형 모양
pts1 = np.array([[100, 100], [200, 100], [200, 200], [100, 200], [150, 150]])
pts2 = np.array([[300, 200], [400, 100], [400, 200]])

#  도형 색깔
cv2.polylines(img, [pts1, pts2], isClosed=True, color=(255, 0, 0))
#  분리하여 색 입히기 가능
# cv2.polylines(img, [pts1], isClosed=True, color=(255, 0, 0))
# cv2.polylines(img, [pts2], isClosed=True, color=(0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
