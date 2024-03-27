# 0205.py
import cv2
from   matplotlib import pyplot as plt

# 이미지 가져오기
imageFile = './data/lena.jpg'
# 이미지 읽기  - 흑백 (cv2.IMREAD_GRAYSCALE)
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

# 윈도우 창 사이즈
plt.figure(figsize=(6,6))
# 이미지 여백
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
# 이미지 보기 - 흑백 (gray)
plt.imshow(imgGray, cmap = 'gray')

plt.axis('off')
# 이미지 저장 -경로 및 이름도 같이
plt.savefig('./data/0205.png')
# 이미지 보기
plt.show()
