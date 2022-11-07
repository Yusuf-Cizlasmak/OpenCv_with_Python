import cv2
import numpy as np

resim = cv2.imread("resim2.png")

#kenarlardan 100 pixel 4 tarafa aynala
resim2 = cv2.copyMakeBorder(resim,300,100,100,100,cv2.BORDER_REFLECT)

#resmi kenarlardan tekrarla
resim3 = cv2.copyMakeBorder(resim,200,200,200,200,cv2.BORDER_WRAP)

#kenarlardan sabit pixelle uzat2
resim4 = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=[125,125,125])

cv2.imshow("orjin",resim)
cv2.imshow("Border Aynalar",resim2)
cv2.imshow("Border Tekrarlama",resim3)
cv2.imshow("Border Uzat",resim4)
cv2.waitKey()
cv2.destroyAllWindows()


###############################################################################
#                  SON PİXELDEN UZATMA
###############################################################################


import cv2
import numpy as np

resim1 = cv2.imread("araba.png")

resim2 = cv2.copyMakeBorder(resim1,200,0,0,600,cv2.BORDER_REPLICATE)

cv2.imshow("Orjinal",resim1)
cv2.imshow("Border Uzatma",resim2)

cv2.imwrite("yeni.png",resim2)

cv2.waitKey()
cv2.destroyAllWindows()