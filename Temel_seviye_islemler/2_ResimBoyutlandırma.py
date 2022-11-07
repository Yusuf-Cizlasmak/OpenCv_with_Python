import cv2


img= cv2.imread("unnamed.png") #resmi okuduk.


img=cv2.resize(img,(360,360))  #gireceğim ilk parametre resmn tutulduğu değişken , ikincisi ise istediğim boyutlar.

# önceki dosyada yazdığım cv2.namedWindow("unnamed",cv2.WINDOW_NORMAL) yazsaydım eğer normal bir şekilde fotoğrafı büyütüp ve küçültebilirdim. 



cv2.imshow("Ana de Armas" , img) #resmi gösterdik
cv2.waitKey(0) #ekranda kaç dakika kalacağını anladık ancak 0 yazdık ya. bir ekrana basana kadar kalır.
cv2.destroyAllWindows() #tüm pencelere zarar vermeden kapatsın.


#####################################################################

#peki biz bir büyütme ve küçültme kodu yazsaydık şayet:


import cv2

def resizewithAspectRatio(img,width=None,height=None,inter=cv2.INTER_AREA):
    dimension=None #dimesion==boyut
    (h,w)= img.shape[:2] #shape fonksiyonu ilk iki değeri ilk olarak SUTUN ve SATIRlardaki piksel sayısını verir.
    
    
    
    if width is None and height is None: # eğer aşağıdaki fonksiyona width(en) veya height(boy) değerlerine girmezsek

        return img #resmi olduğu gibi döndürüyor.
    
    if width is None: #ancak sadece yükseklik için değer girersek
        r = height/ float(h) # girdğimiz height değerini, orjinal h değerine bölüp
        dimension= (int(w*r), height)   #oluşan r değerini en ile çarpıp girdiğimiz height değeriyle birlikte yeni pencere boyutumuz oluyor.
        
    else:
        r= width / float(w) # eğer sadece width girilirse üsttekinin değiştirilmiş hali.
        dimension = (width,int(h*r))
        
    return cv2.resize(img,dimension,interpolation= inter) # işlemler yapıldıktan sonra reSize ile geri döndürme işlemi

img= cv2.imread("unnamed.png")
img1 =resizewithAspectRatio(img,width=None,height=None,inter=cv2.INTER_AREA)  #fonksiyonun kullanımı

cv2.imshow("Original",img)
cv2.imshow("Resized",img1)


cv2.waitKey(0)
cv2.destroyAllWindows()