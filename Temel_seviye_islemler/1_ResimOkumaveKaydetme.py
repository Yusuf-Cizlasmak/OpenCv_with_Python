import cv2 # ilk olarak kütüphanemizi import ederek başlıyoruz. 

#resim okuma

img=cv2.imread("unnamed.png") #resimi derleyicimize aktarma fonksiyonumuz cv2.imread'tir.

cv2.imshow("Image",img)
cv2.waitKey(0) #burada tutulma süresi olarak belirlenir.
#0 girilse herhangi bir tuşa basılmadığı sürece ekranda kalır.
 
cv2.destroyAllWindows() #ram'e zorlamaması için girilen bir fonksiyondur.


#############################################################################################################################



#resim kaydetme

""" yukarıdaki düzene benzer ancak burada imwrite fonk. kullanacağız
    ve burada namedWindow fonksiyonunu da kullanacağız. Bu fonksiyon cv2.WINDOW_NORMAL ile oluşan pencerenin normal görünmesini sağlar.     """

img2=cv2.imread("unnamed.png")
cv2.namedWindow("Image2",cv2.WINDOW_NORMAL) #buraya girilecek ilk argüman pencerenin adı,iki ise penceremin boyutlanması için 

cv2.imwrite("unnamed1.png",img2) #birinci argüman kaydedilecek olan dosya yolu, ikinci değişken olduğudur.


cv2.waitKey(0) #ekranda tutulma süresi.. 0 alırsam ekrana bir tusa basana kadar orada kalır.
cv2.destroyAllWindows()  
