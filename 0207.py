# 0207.py
import cv2

# cap = cv2.VideoCapture(0)  # 0번 카메라
# 비디오 가져오기
cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 프레임 사이즈
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

# 반복을 통한 영상 호출
while True:   
    retval, frame = cap.read()
    # 종료
    if not retval:
        break

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25)
    # 종료
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
# 모든 창 종료
cv2.destroyAllWindows()
