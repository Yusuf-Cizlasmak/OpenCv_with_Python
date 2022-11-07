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
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))#Fonksiyonumuz iki argümanı kabul eder, birincisi structing_elements'in türü. İkincisi ise boyutlarıdır(kernel boyutları).
    #Şayet görüntünü çarpraz bir görüntüden oluşuyorsa : cv2.MORPH_CROSS
    #Yuvarlak bir görüntü için kullanıyorsanız : cv2.MORPH_ELLIPSE gibi tercihler yapabilirsiniz

blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel) #1.parametre uygulanacak resim, 2.parametre = uygulanacak method,3. parametremiz ise Kernel'dir

"""
Görüntüdeki amacımız bir plakayı öne çıkarmaktır. Ve kernel boyutlarımız öncekine nazaran bir tuhaf gelebilir. 
boyutları,Çünkü bir plaka, boyundan kabaca 3 kat daha geniştir!

"""



# sonuçları gösterme
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)


#TOP-HAT

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
cv2.imshow("Tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()