import numpy as np
import argparse
import imutils
import cv2


#görüntüyü kod ekranına çekme ve gri kanala geçirme
image = cv2.imread("barcode_01.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gri kanala çevirme.

#Sobel Filtresinin uygulanması
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

# Y-Gradyan ve X-Gradyan uygulanması
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# Blurlama ve Threshold uygulama
blurred = cv2.blur(gradient, (7, 7)) 
thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)[1] #225'ten küçük olanları siyah, büyük olanları beyazlayıp threshold uyguladık.

#Morfolojik İşlemler
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7)) #kendimize bir kernel oluşturduk . 21,7'lik çünkü barkodlar dikdörtgen yapıda oldukları için.
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#Daha iyi bir nesne tespiti için bazı morfolojik işlemlerin tekrar uygulanması
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

#bunu yapma amacımız Bir erozyon, görüntüdeki beyaz pikselleri "aşındıracak" ve böylece küçük lekeleri kaldıracak, oysa bir genişleme kalan beyaz pikselleri "genişletecek" ve beyaz bölgeleri yeniden büyütecektir.



cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, #Retr_external sadece dış contourları çıkarmak istiyorsanız faydalı olabilir. Aykırı değerleri döndürürken, CHAIN_APPROX_SIMPLE ise sadece uçtaki 4 noktanın konumunu bize verir.
	cv2.CHAIN_APPROX_SIMPLE) #




cnts = imutils.grab_contours(cnts) # barcod'ları yakalama işlemi

for c in cnts:
    epsilon = cv2.arcLength(c, True) #c'den pixsel değerleri alıyor ve kapalı bir cisim için evet diyoruz.
    approx = cv2.approxPolyDP(c, 0.04 * epsilon, True) #ilk parametre değerler,ikinci , 3.parametre kapalı bir alan mı True çeviriyoruz.
    #yukarıdaki iki fonk. kullanımı bakacağınız site :https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html


    x,y,w,h = cv2.boundingRect(approx)#x,y,w,h değerlerinin alınması
    area = cv2.contourArea(c) # contourlanan alanın alanı
    ar = w / float(h) 

    print(f"{area} vs {ar} vs {len(approx)}") #fotoğrafları değerlendirme işlemi


    if len(approx) == 4 and area > 1200 and (ar > .6 and ar < 2):#her yeri barkod olarak almaması ve ROI belirlenmesi
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,12,0), 3) #çizilecek dikdörtgen 
        ROI = image[y:y+h, x:x+w] # REGION OF INTEREST ! 

        cv2.imwrite('ROI.png', ROI)#dosya olarak kaydedelim.


cv2.imshow('image', image)
cv2.imshow('ROI', ROI)

cv2.waitKey(0)
cv2.destroyAllWindows()
