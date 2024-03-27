# 0204.py
import cv2
from   matplotlib import pyplot as plt

# 이미지 가져오기
imageFile = './data/lena.jpg'
# 이미지 읽기 - 흑백으로 가져오기(cv2.IMREAD_GRAYSCALE)
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

# 이미지 보기 and 특성
plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
# 이미지 보기
plt.show()
