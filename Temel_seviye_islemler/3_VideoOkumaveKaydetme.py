import cv2


cap=cv2.VideoCapture("vizontele.mp4")#capture,videoyu VideoCapture ile kod ekranına getiriyoruz.

#videonun framelerin birleşiminden oluştuğunu biliyoruz, bundan dolayı tüm frameleri görmek adına sonsuz bir döngüye sokuyoruz.

while True:
    ret,frame=cap.read() #ret sadece True ve false değerlerini döndürür. Frame ise görüntüleri
    if ret==False:
        print("Görüntü alınamadı")
        break
    cv2.imshow("Vizontele",frame) #yazdırılacak ekran.

    if cv2.waitKey(50) & 0xFF== ord('q'): #waitkey fonksiyonu içindeki sayı 1000/waitkeyİçindekiSayı == Saniye başında Ram'de gösterilecek frame sayısı eşittir.
        #0xFF==ord('q') klavyedeki çıkma tuşunun q'ya atanması
        break

#görüntülerden farklı olarak burada cap.release fonksiyon kullanacağız.
cap.release()
cv2.destroyAllWindows()


######################################################################################################################################
""" Peki videolarınızı tek tuşla istenilen dakikayı fotoğraf olarak kaydetmek ister misiniz ?  """

import cv2
fileName= "vizontele.mp4"
cap = cv2.VideoCapture(fileName) # başka bir camera daha varsa 1 olarak girebilirsiniz.

codec= cv2.VideoWriter_fourcc('M','P','4','V')  #fourcc 4 değer girilmelidir.
frameRate =30 #namına değer Fps
resolution = (640,480) # çözünürlük

videoFileOutput= cv2.VideoWriter(fileName,codec,frameRate,resolution) # codec video algoritmaları tanırlar.


while True:
    
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)# görüntünün eksenlerini değiştiriyor.
    videoFileOutput.write(frame)
    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(20)& 0xFF == ord("d"):   #waitkey fonksiyonu kaç milisaniye görmen gerektiğini gösterir. ve q bastığımda da kapat bir fonksiyon olşturdum
        break

    if cv2.waitKey(30) == ord('s'): # tuşu ile kaydedilmesini sağlar.
        cv2.imwrite("kaydedilecekDosyanınAdı.png",frame)
        
            
videoFileOutput.release()      
cap.release()
cv2.destroyAllWindows() #Rahat kapanmasını sağlar