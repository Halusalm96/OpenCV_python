# 0210.py
import cv2

# 캠 가져오기
cap = cv2.VideoCapture(0) # 0번 카메라
# 프레임 사이즈
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')

# 비디오 출력 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('./data/record0.mp4',fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 20.0, frame_size,isColor=False)

while True:
    retval, frame = cap.read()
    if not retval:
        break   
    out1.write(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)   
    # 이미지 보기  
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)      
    
    key = cv2.waitKey(25)
    if key == 27:
        break

# 종료 (필수)
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
