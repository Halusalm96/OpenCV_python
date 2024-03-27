# 0202.py
import cv2

# 이미지 가져오기
imageFile = './data/lena.jpg'
# 이미지 읽기
img = cv2.imread(imageFile) 
# 이미지 쓰기 - 타입 변경
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])