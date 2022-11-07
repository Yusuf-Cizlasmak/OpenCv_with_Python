###############################################################################
#                           AND, OR, XOR, and NOT bitwise operators
###############################################################################

"""
Bitwise işlemler, maskeler kullanarak görüntülerden belirli ilgi alanlarını çıkarmak için kullanılır.
"""

#Uğraşacağımız resimleri oluşturalım.
# import the necessary packages
import numpy as np
import cv2
# Dikdörtgen çizme
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Dikdortgen", rectangle)
# Yuvarlak çizme
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Yuvarlak", circle)

cv2.waitKey()
cv2.destroyAllWindows()

##AND operatörü

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Bolge ile pixel bitlerini AND türünde eşleştir;"""
"""nesne(11111111) and beyaz(11111111) = sonuç(10111001) yani nesne korundu"""
"""nesne(11111111) and siyah(00000000) = sonuç(00000000) yani background korundu"""

##OR operatörü

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""Bolge ile pixel bitlerini OR türünde eşleştir;"""
"""nesne(11111111) and beyaz(11111111) = sonuç(11111111) yani bembeyaz olur korundu"""
"""nesne(11111111) and siyah(00000000) = sonuç(11111111) yani iki nesne de korundu"""


##XOR operatörü
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""Bolge ile pixel bitlerini XOR türünde eşleştir;"""
"""nesne(11111111) and beyaz(11111111) = sonuç(00000000) yani nesnelerin kesileşen yerleri siyah olur """
"""nesne(11111111) and siyah(00000000) = sonuç(11111111) yani arka plandaki yerler beyaz korundu"""

##NOT

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Daha çok kafa karışıklığı olmaması için TERSLEME olarak düşünebilirsiniz.
"""
