import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\guilh\Documents\AnaliseImagens\Atividade2\Toin.jpg')
toinCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#Filtro Media

blur = cv2.blur(toinCinza,(10,10))

plt.subplot(121),plt.imshow(toinCinza),plt.title('Toin Cinza')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Toin Cinza Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#Filtro Mediana

median = cv2.medianBlur(toinCinza,31)

plt.subplot(121),plt.imshow(toinCinza),plt.title('Toin Cinza')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Toin Cinza Median')
plt.xticks([]), plt.yticks([])
plt.show()

#Filtro Gaussiano

gaussian = cv2.GaussianBlur(toinCinza,(41,41),0)

plt.subplot(121),plt.imshow(toinCinza),plt.title('Toin Cinza')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gaussian),plt.title('Toin Cinza Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()