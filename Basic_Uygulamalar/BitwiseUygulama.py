#Amacımız burada arkaplan ile ay resmini bitwise işlemleri kullanarak birleştirmek

"""
Bitwise işlemleri, maskeler kullanarak görüntülerden belirli ilgi alanlarını çıkarmak için kullanılır.
Maskeler,threshold'un değerlerini belirlenmelidir.
"""



import cv2

#resimleri kod ortamına çekme
img1=cv2.imread('arkaplan.jpeg')
img2=cv2.imread('moon.jpeg')
#Ay resminden ilgilendiğimiz alan(Region of Interest) alanını kadar arkaplandan parça alıp değişkene atayalım.

roi=img1[0:img2.shape[0],0:img2.shape[1]]#en-boy kadar alan alındı
#çıkaracağımız alana maske ve threshold uygulayalım.


img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #gri kanala dönüştürme
mask=cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)[1] #sadece ikinci değeri önemli,ilk değer threshold value döndürecektir.


#bitwise işlemi nesne bulunduktan sonra onu siyah şekline arkaplanı da beyaz yapmak için bitwise_not kullanıyoruz.
mask_inv=cv2.bitwise_not(mask)


# Şimdi ROI'de ayın alanını karartın
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Ay görüntüsünden sadece ayın bölgesini alın.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

#Ekleme işlemi

dst = cv2.add(img1_bg,img2_fg)
img1[0:img2.shape[0], 0:img2.shape[1]] = dst


cv2.imshow('mask',mask)
cv2.imshow('maskinv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('res',img1)

cv2.waitKey()

cv2.destroyAllWindows()
