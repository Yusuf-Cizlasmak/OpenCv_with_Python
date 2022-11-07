###############################################################################
#                           Histogram Eşitleme
###############################################################################
"""
Histogram eşitlemenin yapılış amacı kontrast olarak daha zengin bir imge oluşturmaya çalışmaktır. 
Bu en çok kötü çekilmiş fotoğraflar üzerinde iyileştirme yapılırken kullanılır.
Yani diğer bir deyişiyle nesneleri, görsellerde keskinleştirmek için kullanılır.

Şimdi bir histogram nasıl çizilir ve bunu nasıl eşitlenir bunu göreceğiz.
"""

#Gerekli kütüphanelerin import edilmesi
import numpy as np
import cv2 
from matplotlib import pyplot as plt

path="kagit.jpg"


image=cv2.imread(path)



#resmi tek kanala indirme
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#pixelleri alma 
y_pixels=image.shape[0] 
x_pixels=image.shape[1] 

#pixelleri düzleşttirme (FLATTEN)

#Sutün vektör


flattened=image.reshape([x_pixels*y_pixels]) 
#bunun yerine img.ravel()'da kullanılabilirdi.img.ravel() fonksiyonu tüm pixel değeri düz bir vektör haline getirir.


#histogram grafiği çizme
plt.hist(flattened,bins=256) #256 değerlere kadar gösterme
plt.show()


#32 bidonlara kadar oluşturma evet 32 bidon !
plt.hist(flattened,bins=32)
plt.show()






#HISTOGRAM equalize(histogram eşitleme)


equalized = cv2.equalizeHist(image)

#pixelleri alma 
y_pixels_eq=equalized.shape[0]
x_pixels_eq=equalized.shape[1]



flattened_eq=equalized.reshape([x_pixels_eq*y_pixels_eq])


#histogram grafiği çizme

plt.hist(flattened,bins=256) #256 değerlere kadar gösterme
plt.hist(flattened_eq,bins=256) #256 değerlere kadar gösterme
plt.show()


#32 bidonlara kadar oluşturma evet 32 bidon !
plt.hist(flattened_eq,bins=32)
plt.show()



cv2.imshow("Input", image)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)


####BİR BAŞKA YÖNTEM!!!

# CLAHE (Contrast Limited Adaptive Histogram Equalization) methodu

print("applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit = 1) # clipLimit -> Threshold for contrast limiting
final_img = clahe.apply(image) + 13 


cv2.imshow("Input", image)
cv2.imshow("CLAHE method Histogram Equalization", final_img)
cv2.waitKey(0)


####################################################################################


img = cv2.imread(path,0)

#To display image before equalization
cv2.imshow('image',img)
cv2.waitKey(0)


a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16) 

height,width=img.shape

#finding histogram
for i in range(width):
    for j in range(height):
        g = img[j,i] 
        a[g] = a[g]+1 
        

print(a)   


#performing histogram equalization
tmp = 1.0/(height*width)
b = np.zeros((256,),dtype=np.float16)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp
    b[i] = round(b[i] * 255)

# b now contains the equalized histogram
b=b.astype(np.uint8)

print(b)

#Re-map values from equalized histogram into the image
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()