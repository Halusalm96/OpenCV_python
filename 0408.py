# 0408.py
import cv2
import os

# 현재 스크립트가 실행되는 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일의 절대 경로를 생성합니다.
img_path = os.path.join(current_dir, './data/lena.jpg')

src = cv2.imread(img_path,  cv2.IMREAD_GRAYSCALE) 

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# 마우스로 여러개의 박스를 만들어 지정할 수 있는 함수
rects = cv2.selectROIs('src', src, False, True)
print('rects =', rects)

for r in rects:
    cv2.rectangle(src, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)    
##    img = src[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
##    cv2.imshow('Img', img)
##    cv2.waitKey()

cv2.imshow('src', src)
cv2.waitKey()    
cv2.destroyAllWindows()
