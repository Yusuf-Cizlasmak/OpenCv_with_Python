###############################################################################
#                           Morfolojik İşlemler
###############################################################################

import argparse
import cv2

"""
kodun bulduğu kaynak dosyasına girip oradan ,
-->python dosyaİsmi.py --image(key) resimİsmi.png(value)

yapabilirsiniz.
"""



ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input image")
args=vars(ap.parse_args())


### ERODE ### 

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
#Uygulanan erode işleminin resimdeki değişimi
for i in range(0, 3):
	eroded = cv2.erode(gray.copy(), None, iterations=i + 1) #ilk parametre uygulanacak resim, ikinci parametremiz structing element, (None kullanırsanız : 8 tane komşusuna bakıp-(4'lü olanı da vardır. Opsiyonel olarak kendi structing element'inizi kullanabilirsiniz), 3×3'lük bir kernel matrisi kullanılacaktır.)
    #Son parametremiz ise kaç defa uygulanacağıdır.
	cv2.imshow("Erode işlemi {} defa uygulandi".format(i + 1), eroded)
	cv2.waitKey(0)


### DILATION ### 

cv2.destroyAllWindows()
cv2.imshow("Original", image)


# Uygulanan dilation işleminin resimdeki değişimi
for i in range(0, 3):
	dilated = cv2.dilate(gray.copy(), None, iterations=i + 1) #ilk parametre uygulanacak resim, ikinci parametremiz structing element, (None kullanırsanız : 8 tane komşusuna bakıp-(4'lü olanı da vardır. Opsiyonel olarak kendi structing element'inizi kullanabilirsiniz), 3×3'lük bir kernel matrisi kullanılacaktır.)
    #Son parametremiz ise kaç defa uygulanacağıdır.
	cv2.imshow("Erode işlemi {} defa uygulandi".format(i + 1), dilated)
	cv2.waitKey(0)


### OPENING ### 


cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)] #Structing_Element yükseklik ve genişliğini belirtir.
# Her kernel'in etkisini görmek için:
for kernelSize in kernelSizes:
	#Kendime bir structing_element oluşturdum.
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize) #Fonksiyonumuz iki argümanı kabul eder, birincisi structing_elements'in türü. İkincisi ise boyutlarıdır.
    #Şayet görüntünü çarpraz bir görüntüden oluşuyorsa : cv2.MORPH_CROSS
    #Yuvarlak bir görüntü için kullanıyorsanız : cv2.MORPH_ELLIPSE gibi tercihler yapabilirsiniz

    
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)

#Daha önceden belirttiğimiz gibi karıncalı resimlerde, nesneyi öne çıkarmak isterseniz gayet kullanışlı bir işlemdir.


### CLOSING ### 

cv2.destroyAllWindows()
cv2.imshow("Original", image)
# # Her kernel'in etkisini görmek için:
for kernelSize in kernelSizes:
	# 
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({}, {})".format(
		kernelSize[0], kernelSize[1]), closing)
	cv2.waitKey(0)

#Adından da anlaşılacağı gibi, nesnelerin içindeki delikleri kapatmak veya bileşenleri birbirine bağlamak için bir kapatma kullanılır.


### Morfolojik Gradyan ### 
cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    gradient=cv2.resize(gradient,(480,480))

    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)

    cv2.waitKey(0)

#Morfolojik gradyan, bir görüntünün genişlemesi ile erozyona uğraması arasındaki farktır.Bu sayede görüntünün kenarlarının bulunmasını sağlayabiliriz



