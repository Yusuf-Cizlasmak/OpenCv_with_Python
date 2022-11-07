###############################################################################
#                 Canvas=Tuval Oluşturma
###############################################################################

import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) #çizdiğimiz siyah tuvalın boyutları 512'e 512 olup BGR şeklinde 3 kanalı mevcuttur.
#np.zeros amacı da belli bir alanı siyaha bulamaktır.1-2 tuvalin boyutunu verirken,3.değişken kanalı işaret eder.
cv2.imshow("tuval",canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()

###############################################################################
#                 Canvas=Tuval Rengini değiştirme
###############################################################################

#tuvali hepsini kırmızı renk yapma

canvas[:]=(0,0,255) #burada numpy temel özelliklerinden birini kullanarak for döngüsüne gerek kalmadan tüm pixelleri kırmızıya boyuyoruz.

cv2.imshow("tuval",canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()



#bir kısmını boyamak istersek

img= np.zeros((10,10),np.uint8) #burda 10'a 10'luk bir siyah alanımı oluşturdum sonra siyah-beyazsa  3lük bir kanal oluşturmaya gerek yok.. np.uint8'de benim veri tipim

img[0,0]= 255
img[0,1]= 200   
img[0,2]= 65
img[0,3]= 15

#img= np.zeros((10,10,3),np.uint8) #renklilerde..

#img[0,0]= (255,255,255)
#img[0,1]= (255,255,200)
#img[0,2]= (255,255,65)
#img[0,3]= (255,255,15)

img= cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA) #burda yeniden boyutlandırdım img'yi.interpolation birtakım çakışmaları engellemek için her resize fonksiyonunda kullanmak lazım..
cv2.imshow("kanvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()