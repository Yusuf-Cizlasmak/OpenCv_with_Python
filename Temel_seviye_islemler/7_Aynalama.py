import cv2
import numpy as np

resim1 = cv2.imread("araba.png")
boy, genişlik, kanal = resim1.shape

resim2 = cv2.flip(resim1,0)   #vertical
resim3 = cv2.flip(resim1,1)   #horizantal
resim4 = cv2.flip(resim1,-1)  #orjine göre flip

cv2.imshow("Orjinal",resim1)
cv2.imshow("Dikey Ayna",resim2)
cv2.imshow("Dusey Ayna",resim3)
cv2.imshow("Orjine göre çift flip",resim4)
cv2.waitKey()
cv2.destroyAllWindows()


# linner cebir 
#OpenCV'si görüntüleri NumPy dizisi olarak işler 

#0, x ekseni etrafında çevirme anlamına gelir 

#y ekseni etrafında çevirme anlamına gelir.

#Negatif değer (örneğin, -1), her iki eksenin etrafında çevrilmesi anlamına gelir.

#2B diziyi çevirmek için cv2.flip() yöntemi kullanılır.

#OpenCV ile görüntüyü döndürün:cv2.rotate()

#OpenCV ile görüntüyü çevirin:cv2.flip()

#NumPy ile görüntüyü döndürün:np.rot90()

#NumPy ile görüntüyü çevirin:np.flip()