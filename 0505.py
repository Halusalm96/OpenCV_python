# 0505.py
import cv2
import numpy as np
from   matplotlib import pyplot as plt
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, 'data', 'lena.jpg')

src = cv2.imread(img_path)

# src = cv2.imread('./data/lena.jpg')

histColor = ('b', 'g', 'r')
for i in range(3):
    hist = cv2.calcHist(images=[src], channels=[i], mask=None,
                    histSize=[256], ranges=[0, 256])
    plt.plot(hist, color = histColor[i])    
plt.show()
