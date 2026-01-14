# Görüntü İşleme ile Kalite Kontrol Projesi

Bu projeyi Elektrik Elektronik Mühendisliği eğitimim sırasında üretim bantlarındaki otomasyon mantığını kavramak için geliştirdim.

  Projenin Amacı
Kameradan gelen görüntüyü analiz ederek, belirlediğim kriterlere (renk ve boyut) uyan ürünleri tespit etmek ve "Sağlam/Hatalı" ayrımı yapabilmek.

  Kullandığım Teknolojiler
-Python (Yazılım dili)
-OpenCV (Görüntü işleme kütüphanesi)
-NumPy (Matematiksel işlemler için)

  Nasıl Çalışır?
1. Kod çalıştırıldığında webcam açılır.
2. Görüntü HSV formatına çevrilerek renk filtrelemesi yapılır (Yeşil renk).
3. Gürültü temizleme işlemlerinden sonra nesne tespit edilirse ekrana "ONAYLANDI" yazar.
