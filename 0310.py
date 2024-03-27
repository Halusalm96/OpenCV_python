#0310.py
import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0 # right

while True:   
    key = cv2.waitKeyEx(30)    
# 키 값 확인
    print(key)
    # 키 값 확인을 통한 값 정리 (이중에 1택)
    # W=119 / A=97 / S=115 / D=100
    # I=105 / J=106 / K=107 / L=108
    # 8=56 / 4=52 / 2=50 / 6=54
    if key == 0x1B: 
        break;

# 방향키 방향전환 
    elif key == 0x64: # right
        direction = 0
    elif key == 0x73: # down
        direction = 1
    elif key == 0x61: # left
        direction = 2
    elif key == 0x77: # up
        direction = 3
        
# 방향으로 이동 
    if direction == 0:     # right
        x += 10
    elif direction == 1:   # down
        y += 10
    elif direction == 2:   # left
        x -= 10
    else: # 3, up
        y -= 10
        
#   경계확인 
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3
        
# 지우고, 그리기        
    img = np.zeros((width, height,3), np.uint8) + 255 # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1) 
    cv2.imshow('img', img)
    
cv2.destroyAllWindows()
