import cv2

image=cv2.imread("coin.png")

###############################################################################
#                           EŞİKLEME(THRESHOLD) İŞLEMLERİ
###############################################################################



#Gauss bulanıklaştırma uygulamak, görüntüdeki ilgilenmediğimiz bazı yüksek frekanslı kenarların kaldırılmasına yardımcı olur ve daha “temiz” bir segmentasyon elde etmemizi sağlar.
blurred = cv2.GaussianBlur(image, (3, 3), 0)

# ilk parametre uygulanacak görüntü
#ikinci parametremiz eşik değeri (thresh eşik değeri)
# üçüncü değerimiz max değer(ki bu 255 eşit.)
#dördüncü parametremiz ise ters eşikleme anlamına geliyor.
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
#ilk çıktımız Threshold value, ikincisi de threshold uygulanmış resim olarak görebilirsiniz.


#cv2.ADAPTIVE_THRESH_MEAN_C : Eşik Değeri = (Komşu alan değerlerinin ortalaması – sabit değer).
# Başka bir deyişle ,blockSize×blockSize komşuluğunun ortalamasıdır.

#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : Eşik Değeri = (Mahalle değerlerinin Gauss ağırlıklı toplamı – sabit değer).
# Başka bir deyişle,blockSize×blockSize komşuluğunun ağırlıklı toplamıdır.

#blockSize  = Bir eşik değeri hesaplamak için kullanılan piksel komşusunun boyutu=11
#sabit=Komşu piksellerin ortalama veya ağırlıklı toplamından çıkarılan sabit bir değer
#11 boyutlu kareler ile 8 constant değerinde eşik ortalamaları al ve maskele

#farklı threshold metotları, alternatif denenebilir;
#ret,maske = cv2.threshold(griLogo,min,255,cv2.THRESH_TRUNC)
#ret,maske = cv2.threshold(griLogo,min,255,cv2.THRESH_TOZERO)(Subu-ai)





cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




###############################################################################
#                           OTSU ALGORİTMASI
###############################################################################


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)


(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("Threshold value değerimiz: {}".format(T)) # Bulunan Threshold değerinin ekrana yazılması.
# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv) # Görüntünün üzerine yazmak istiyorsak şayet.
cv2.imshow("Output", masked)
cv2.waitKey(0)
"""Bolge ile maskenin pixel bitlerini AND türünde eşleştir"""
"""beyaz arkaplanı olan maske ile arkaplandaki pixel eşleri için;"""
"""background(10111001) and beyaz(11111111) = sonuç(10111001) yani arkaplan korundu"""
"""background(10111001) and siyah(00000000) = sonuç(00000000) yani siyah nesne korundu"""


###############################################################################
#                           Adaptive Threshold
###############################################################################


# uyumlu eşik fonksiyonu (arkaplandan ayrışması zor olan nesnelerde kullanılabilir)
maske2 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
#11 boyutlu kareler ile 8 constant değerinde eşik ortalamaları al ve maskele



