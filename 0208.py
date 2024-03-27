# 0208.py
import cv2

# 안드로이드 카메라 가져오기
cap = cv2.VideoCapture('http://172.30.1.18:4747/mjpegfeed') # droid cam
##cap = cv2.VideoCapture('http://172.30.1.18:4747/mjpegfeed?640x480')
##cap = cv2.VideoCapture('http://172.30.1.18:8080/video')  # IP Webcam

# 프레임 사이즈
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

# 반복을 통해 영상 호출
while True:   
    retval, frame = cap.read() # 프레임 캡처
    # 종료
    if not retval:
        break

    cv2.imshow('frame',frame)
    
    # 25초 기다리기
    key = cv2.waitKey(25)
    # 종료
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
# 모든 창 종료
cv2.destroyAllWindows()
