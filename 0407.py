# 0407.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path,  cv2.IMREAD_GRAYSCALE)

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# 마우스로 지정한 곳의 값을 저장하는 함수
roi = cv2.selectROI(src)
print('roi =', roi)

# 마우스로 지정했다면 보이게 하는 함수
if roi != (0, 0, 0, 0):
    img = src[roi[1]:roi[1]+roi[3],
               roi[0]:roi[0]+roi[2]]

    cv2.imshow('Img', img)
    cv2.waitKey()
    
cv2.destroyAllWindows()
