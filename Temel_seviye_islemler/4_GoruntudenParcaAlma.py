import cv2
import numpy as np
###############################################################################
#                     Resim okuma
###############################################################################
resim=cv2.imread("resim.png")
cv2.imshow("resim",resim)
cv2.waitKey()
cv2.destroyAllWindows()
###############################################################################
#                  Gray kanalda img okuma   
###############################################################################
resim = cv2.imread("resim.png",0)  #--> 0 parametresi resmi gri tonlarında okur
cv2.imshow("resim",resim)
cv2.waitKey()
cv2.destroyAllWindows()
###############################################################################
#                  Pixel konumu ile renk listesini alma  
###############################################################################
pixel = resim[100,200]    
print(pixel) 
print(resim.shape)
###############################################################################
#                  BGR Kanallarına  Ayırma 
###############################################################################

#sadece belli renk değerlerini alma
# b,g,r = cv2.split(resim)
# print(b)
# cv2.imshow("blue chanel",b)
# cv2.imshow("green chanel",g)
# cv2.imshow("red chanel",r)
# cv2.waitKey()
# cv2.destroyAllWindows()
###############################################################################
#                   Görüntüden belli parça alma 
###############################################################################
parça = resim[0:400,0:400]   #resim[x1:x2,y1,y2]
cv2.imshow("Parça_alma ",parça)
cv2.waitKey()
cv2.destroyAllWindows()
###############################################################################
#               Çoklu Pixel Değiştirme  
###############################################################################

parça2 = resim[500:600,0:400]  #genişlik , yükseklik
resim[0:100,0:400] = parça2

cv2.imshow("Parca 2",parça2)
cv2.imshow("Penceremiz",resim)
cv2.waitKey()
cv2.destroyAllWindows()
###############################################################################
