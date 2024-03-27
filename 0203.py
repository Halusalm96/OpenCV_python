# 0203.py
import cv2
from   matplotlib import pyplot as plt

# 이미지 가져오기
imageFile = './data/lena.jpg'
# 이미지 읽기
imgBGR = cv2.imread(imageFile)
plt.axis('off')

# 이미지 칼라로 가져오기
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
# 이미지 보기
plt.imshow(imgRGB)
# 윈도우창에 이미지 보이기
plt.show()
