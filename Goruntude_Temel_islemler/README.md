## MORFOLOJİK İŞLEMLER
Morfolojik görüntü işleme şekillerin biçimsel yapısı ile ilgilenerek nesneleri ayırt etmemize ve gruplayabilmemize olanak sağlar. Yöntem gri seviye görüntüler üzerinde de çalışsa da genellikle siyah-beyaz (ikili) görüntüler üzerinde kullanılır.Peki neden öğrenmeliyiz? 
Çünkü bu dönüşümler oldukça güçlüdür.

![1](https://user-images.githubusercontent.com/97342455/200417857-a8c633f4-71f3-41d1-87ba-a955587abc15.png)

Morfoloji (İngilizce morphology) şekil bilimi olarak tanımlanmaktadır. 
Başlı başına bilim olan bu alanı tüm yöntemleri ile OpenCV Kütüphanesi içerisine taşımak elbette ki mantıklı bir seçim değildir bu yüzden ihtiyaç duyulabilecek bazı teknikler aktarılmıştır.

Bunlar:

- Erosion (Aşındırma)
    
    Bir nehir kıyısından akan suyun toprağı aşındırması gibi, bir görüntüdeki aşınma da ön plandaki **nesneyi "aşındırır" ve onu küçültür.** Basitçe söylemek gerekirse, bir görüntüdeki bir nesnenin sınırına yakın pikseller atılır ve onu “aşındırır”.
    
    ![2](https://user-images.githubusercontent.com/97342455/200418215-f510fb2d-c35a-42b5-94ec-d924f31e2806.png)
    
    Yine, erozyonlar, bir görüntüden **küçük lekeleri çıkarmak veya birbirine bağlı iki bileşenin bağlantısını kesmek için en kullanışlıdır.**
    
- Dilation (Yayma – Genişletme)
    
    Erozyonun tersi genişlemedir. Tıpkı bir erozyonun ön plan piksellerini yiyip bitirmesi gibi, bir genişleme de ön plan piksellerini büyütecektir.
    
    ![3](https://user-images.githubusercontent.com/97342455/200418345-bbf9cc2b-86b2-4490-a3ed-0ac7a4e3adbf.png)
    
    Genişletmeler, ön plan nesnelerinin boyutunu artırır ve özellikle görüntünün kırık parçalarını birleştirmek için kullanışlıdır.
    
- Opening (Açınım)
    
    **Erosion ve dilation operatörlerinin görüntü üzerine birlikte uygulanması ile gerçekleşir. Öncelikli olarak erosion operatörü uygulanır ve ardından dilation operatörü uygulanır**.
    
    ![4](https://user-images.githubusercontent.com/97342455/200418475-6541e873-6a9a-4fb2-81e4-6d7de4df52c1.png)


    Kirli olan görüntülerde ilk önce erozyon ile görüntülerden kurtulur ve dilate ile nesne büyütülmeye çalışılır.Bu tip gibi durumlarda oldukça çok işe yarar.
    
- Closing (Kapanım)
    
    Opening tam tersi bir Closing olacaktır. Closing , dilate uygulandıktan sonra ardından erozyon uygulanır.**Adından da anlaşılacağı gibi, nesnelerin içindeki delikleri kapatmak veya bileşenleri birbirine bağlamak için bir kapatma kullanılır.**
    
    ![5](https://user-images.githubusercontent.com/97342455/200418577-525faf19-3b98-415b-b193-28b1f88175fe.png)

    
- Morphological Gradient
    
    Morfolojik gradyan, **bir görüntünün genişlemesi ile erozyona uğraması arasındaki farktır.**Bu sayede görüntünün kenarlarının bulunmasını sağlayabiliriz
    
    ![6](https://user-images.githubusercontent.com/97342455/200418834-a61558c4-49e8-4f39-9cb5-722d3f20b97d.png)

    
- Top Hat-Black Hat
  
  Top Hat,morfolojik işlem, orijinal (gri tonlamalı/tek kanallı) giriş görüntüsü ile opening görüntüsü arasındaki farktır,koyu arka planlar üzerinde bir görüntünün parlak bölgelerini ortaya çıkarmak için kullanılır.
   ![7](https://user-images.githubusercontent.com/97342455/200419250-611ee7b1-cd1f-4c89-b851-2359076a16d7.png)
   
   
   
  https://medium.com/@ycizlasmak/opencv-ile-morfolojik-i̇şlemler-48cb0cceda94
