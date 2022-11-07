###################### İmport Library ########################################
import cv2
##############################################################################
#             Resmi Dijital Numpy Dizisine Çevirerek Oku
###############################################################################
resim = cv2.imread("resim.png") #resmi dijital numpy dizisine çevirerek oku
cv2.imshow("Pencere",resim)

###############################################################################
#              RESİM BOYUT - PİXEL SAYISI
###############################################################################
img_info = resim.shape   # 568 x 270 genişlik ve boy, 3 (RGB) renk kanallı
img_pixels = resim.size    # genişlik x boy x kanal = pixel_sayısı
print(img_info,img_pixels)

###############################################################################  

key = cv2.waitKey()# yazmazsan resim 60 hz  1 kere gözükür
# resim açıkken herhangi bir tuşa basılana kadar beklet
# hangi tuşa basılırsa o tuş karakterinin onluk (decimal) int çıktısını verir

if key == 27:
    print("ESC ye basıldı.")
    cv2.destroyAllWindows()
if key == ord("q"):   #q tuşunu decimal'e çevir
    print("q ye basıldı.")
    cv2.imwrite("yeni_resim.png",resim) ## numpy olarak rame kaydetme 
    
    
cv2.destroyAllWindows() 
#ram de üzerine sürekli yazan imshowun tüm pencerelerini kapatmayı sağlar.
#(üzerine yazmayı engellemesini sağlar)