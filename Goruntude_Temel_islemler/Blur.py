###############################################################################
#                           RESİM YUMUŞATMA (BULANIKLAŞTIRMA-BLURRING)
###############################################################################

"""
Görüntü işlemede, filtreler görüntüyü yumuşatmak yada kenarları belirginleştirmek için dijital filtreler
kullanılır. Bu bölümde resim yumuşatma ele alınacaktır. 

• Ortalama Filtre (Mean):
• Orta Değer Filtresi (Median)
• Gauss düzleştirme Filtresi (Gaussian Smoothing)
"""

import cv2


image = cv2.imread("byd.jpg")
image=cv2.resize(image,(480,480))
cv2.imshow("Original", image)

##Ortalama Filtre (Mean)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
# KernelSize teker teker görülmesi döngü oluşturulması
for (kX, kY) in kernelSizes:

	blurred = cv2.blur(image, (kX, kY)) #1.parametre uygulunacak resim, ikinci kernelSize
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)
cv2.destroyAllWindows()
#Burada kernel ortasındaki ortalamaya göre matrisin pixellerin ortalaması değiştirir.

#Genellikle görüntülerdeki gürültüyü azaltmak için kullanılır.


#Gauss düzleştirme Filtresi (Gaussian Smoothing)
for (kX, kY) in kernelSizes:

	blurred = cv2.GaussianBlur(image, (kX, kY),sigmaX=0) #1.parametre uygulunacak resim, ikinci kernelSize,sigmaX gaussian Blur özel bir parametredir.
	cv2.imshow("Gaussian Blur :Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)
cv2.destroyAllWindows()



#Orta Değer Filtresi (Median)
#diğerlerinden farklı olarak sadece tekli kernel_size alır.

# KernelSize teker teker görülmesi döngü oluşturulması
for k in (3, 9, 15):
	blurred = cv2.medianBlur(image, k)
	cv2.imshow("Median {}".format(k), blurred)
	cv2.waitKey(0)
cv2.destroyAllWindows()



## EKSTRA  Bilateral Filtering:
for k in (3, 9, 15):
    blurB= cv2.bilateralFilter(image,k,sigmaColor=95,sigmaSpace=95)
    cv2.imshow("Bilateral {}".format(k), blurB)
    cv2.waitKey(0)


cv2.destroyAllWindows()