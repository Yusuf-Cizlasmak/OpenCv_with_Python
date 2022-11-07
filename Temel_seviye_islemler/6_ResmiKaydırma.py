
###############################################################################
#                  SON PİXELDEN UZATMA
###############################################################################

import cv2
import numpy as np

img= cv2.imread("unnamed.png",0)  # neden yanına 0 koydum çünkü bu foto görüntülü ben bunda daha kolay işlem yapmak için gray çevirdim.
#ben bunun en-boy ölçülerini görmek için img.shape fonksiyonundan yararlanıcam.bunları row ve col ile yapıcam row satır demek.

row,col=img.shape
print(col)
print(row)
#Matris için büyük bi M değişkeni tanıyıp 1,0, kendi x değerim sonra da aynı şeyi


M= np.float32([[1,0,100],[0,1,70]]) #1-0 ve 0-1 düzlemi belirler.

#sondakii değerleri artıkça daha kayıyor resim.

dst= cv2.warpAffine(img,M,(512,213)) #burada wapAffine fonksiyonu ile resmi istediğim kadar kaydırabiliyorum. ilk indexim uygulacağım resim, sonraki M(atrisim), en sonunda da yeni şeklin koordinatlarını veriyorum img.shape'in değerleri olacak.

cv2.imshow("Matrisli",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()