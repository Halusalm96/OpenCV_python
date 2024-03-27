# 0401.py
import cv2
import numpy as np
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

img = cv2.imread(img_path) 

# img = cv2.imread('./data/lena.jpg') # cv2.IMREAD_COLOR
##img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# 몇 차원인지 알려주는 함수
print('img.ndim=', img.ndim)
# 차원을 자세히 말해주는 함수
print('img.shape=', img.shape)
# 차원의 타입을 말해주는 함수
print('img.dtype=', img.dtype)

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
# 타입 변환
img=img.astype(np.int32)
print('img.dtype=',img.dtype)

img=np.uint8(img)
print('img.dtype=',img.dtype)
