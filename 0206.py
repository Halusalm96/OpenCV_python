# 0206.py
import cv2
from   matplotlib import pyplot as plt

# 이미지 가져오기 위한 베이스
path = './data/'
# 이미지 가져오고 읽기
imgBGR1 = cv2.imread(path+'lena.jpg')
imgBGR2 = cv2.imread(path+'apple.jpg')
imgBGR3 = cv2.imread(path+'baboon.jpg')
imgBGR4 = cv2.imread(path+'orange.jpg')

# 이미지 칼라로 설정
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

# 윈도우 창의 사이즈 및 이름
fig, ax = plt.subplots(2, 2, figsize=(10,10), sharey=True)
fig.canvas.manager.set_window_title('Sample Pictures')

# 각 이미지의 위치
ax[0][0].axis('off')
ax[0][0].imshow(imgRGB1, aspect = 'auto')

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'auto')

ax[1][0].axis("off")
ax[1][0].imshow(imgRGB3, aspect = "auto")

ax[1][1].axis("off")
ax[1][1].imshow(imgRGB4, aspect = 'auto')

# 윈도우창의 이미지 사이의 여백 사이즈
plt.subplots_adjust(left=0, bottom=0, right=1, top=1,
                    wspace=0.05, hspace=0.05)
# 정리된 이미지 사진 저장
plt.savefig("./data/0206.png", bbox_inches='tight')
# 이미지 보기
plt.show()
