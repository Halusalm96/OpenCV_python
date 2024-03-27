# 0201.py
import cv2

# 이미지 가져오기
imageFile = './data/lena.jpg'

# 이미지 읽어오기
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
# 0이 들어가서 흑백으로 변경
img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE
# 창 띠우기
cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

# option : data 분석 코드
print("img value : ", img)
cv2.waitKey()
print("type(img) : ", type(img))
print("img.shape : ", img.shape)
print("img.view : ", img.view)

# 키보드 입력하면 작동
cv2.waitKey()
# 모든 창을 종료
cv2.destroyAllWindows()