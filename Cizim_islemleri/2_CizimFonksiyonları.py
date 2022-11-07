###############################################################################
#                 Boş Tuvale çizgi-dikdörtgen-yuvarlak çizme işlemleri
###############################################################################

import cv2
import numpy as np


canvas=np.zeros((512,512,3),dtype=np.uint8)+255

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5 )
cv2.line(canvas,(100,50),(200,250),(0,0,255),thickness=9 )
#ilk başta resmi yapacagımız canvas'ı(tuvali) girmemiz gerekiyor. sonra başlangıç ve son değerini girilir sonra da renk ve en son kalınlık(thickness=) değeri girilir.

cv2.rectangle(canvas,(20,20),(70,70),(0,255,0),thickness=-1)
#peki ya ben dikdörtgenim içini dolu yapmak istiyorsam..thickness -1 değeri gir ve sonuca bak  :)
cv2.rectangle(canvas,(10,10),(250,250),(0,255,255),thickness=-3)


#şimdi de yuvarlak çizelim..ilk başta merkezin konumunu,sonra yarıçapını,rengini ve kalınlık değerlerini girmem gerekiyor.

cv2.circle(canvas,(250,250),100,(0,133,0),thickness=-4) #- olması içinin dolu olmasını sağlar.

#peki ya üçgen ?? üç nokta belirle ona göre cv2.line ile birleştirme bir yöntem olabilir.
p1=(100,200)
p2=(50,70)
p3=(280,65)

cv2.line(canvas,p1,p2,(0,55,0),thickness=9)
cv2.line(canvas,p1,p3,(0,55,0),thickness=9)
cv2.line(canvas,p2,p3,(0,55,0),thickness=9)


#peki diğer büyük şekilleri mesela beşgen gibi ifadelerinde de cv2.polylines ile kullanıyorum..

cv2.imshow("canvas",canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()