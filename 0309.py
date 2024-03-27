#0309.py
import numpy as np
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# 문자열
text = 'OpenCV Programming'
# 위치 (글자 좌측 아래)
org = (50,100)
# 폰트
font = cv2.FONT_HERSHEY_SIMPLEX
# 문자열 출력 - (이미지, 글자, 위치, 폰트, 글자크기, 색, 굵기)
cv2.putText(img,text, org, font, 1, (255,0,0), 2)

# 문자열 사이즈 보기 - (글자, 폰트, 글자크기, 굵기)
size, baseLine = cv2.getTextSize(text, font, 1, 2)
print('size=', size)
print('baseLine=', baseLine)
# 문자열 크기에 따른 직사각형 그리기 - (이미지, 위치, 대각점의 위치, 색)
# (org[0]+size[0], org[1]-size[1]) = (395,78)
cv2.rectangle(img, org, (org[0]+size[0], org[1]-size[1]), (0, 0, 255))
# 문자열 위치를 원으로 그리기 - (이미지, 위치, 크기, 색, 두께)
cv2.circle(img, org, 3, (0, 255,0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
