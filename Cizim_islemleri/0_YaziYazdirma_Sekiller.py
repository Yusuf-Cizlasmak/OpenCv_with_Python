import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8)+254

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX  


cv2.putText(canvas,"OpenCV",(100,99),font1,4,(255,0,0),cv2.LINE_AA) #en sondaki rastgele yazı tipi..
#Burda ilk başta yazı yazacağım değişkenim ,sonra yazacağım texti,yazıyı yazacağım ilk konumu,sonra büyüklüğü ve rengi ve en son tipi,sonra 2. konum ve büyüklüğü..,sonra 3...



cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

###############################################################################
#                           Çizgi Çizme
###############################################################################
import cv2
import numpy as np

image = cv2.imread("unnamed.png")

p1 = (0,50)     # (sütun,satır)
p2 = (200,50)
color = [0,200,0] #Blue-Green-Red
thickness = 4
cv2.line(image,p1,p2,color,thickness)

cv2.imshow("Pencere",image)
cv2.waitKey()
cv2.destroyAllWindows()

###############################################################################
#                           Dikdörtgen Çizme
###############################################################################

import cv2
import numpy as np

image = cv2.imread("unnamed.png")

point1 = (100,200)    #(sütun,satır)  dikdörtgen sol üst konumu
point2 = (400,500)   #(sütun,satır)  dikdörtgen sağ alt konumu
 
cv2.rectangle(image,point1,point2,color=[0,0,255],thickness=-1)

cv2.imshow("Pencere",image)
cv2.waitKey()
cv2.destroyAllWindows()

###############################################################################
#                           Yuvarlak Çizme
###############################################################################
import cv2
import numpy as np

image = cv2.imread("unnamed.png")

radius=30

cv2.circle(image,(170,65),radius=radius,color=(0,255,255),thickness=-1)

cv2.imshow("Yuvarlak",image)
cv2.waitKey()
cv2.destroyAllWindows()