# 0209.py
'''
# 설치해야 실행 가능
 pip install youtube_dl
 pip install pafy
'''
import cv2, pafy
# 유튜브 영상 가져오기
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
# 유튜브 영상 읽기
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest() # video.getbest(preftype='mp4')
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)
# 반복으로 영상 호출
while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame',frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)
        cv2.imshow('edges',edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break
cv2.destroyAllWindows()
