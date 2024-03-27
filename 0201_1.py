import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)  # 이미지 파일 읽기

# 이미지가 비어 있는지 및 크기를 확인
if img is not None and img.size > 0:
    # 이미지가 비어 있지 않고 크기가 0보다 크면 imshow 호출
    cv2.imshow('Lena color', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("이미지를 읽을 수 없습니다.")
