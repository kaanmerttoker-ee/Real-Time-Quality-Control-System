import cv2
import numpy as np

# kamerayı burda başlatıyorum. 0 genelde labtopun kendisi oluyor
kamera = cv2.VideoCapture(0)

print("Kamera acildi... Yesil renk goster bana")

while True:
    # kameradan anlık goruntu aliyoz
    basarili_mi, goruntu = kamera.read()
    
    # eger kamera acilmazsa donguyu kirip ciksin hata vermesin
    if not basarili_mi:
        break

    # burda goruntuyu hsv formatina ceviriyoz cunku renkleri boyle daha iyi ayirt ediyo
    hsv_format = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    # YESIL rengin kodlari (bunu internetten buldum yesil tonlari icin)
    # biraz genis aralik verdim ki isiktan etkilenmesin
    alt_sinir = np.array([40, 70, 70])
    ust_sinir = np.array([80, 255, 255])

    # maskeleme islemi: sadece yesil olan yerleri beyaz yap gerisini siyah birak
    maske = cv2.inRange(hsv_format, alt_sinir, ust_sinir)

    # goruntudeki karıncalanmaları temizlemek icin (gürültü filtresi)
    # yoksa kucuk noktalarida nesne saniyo
    maske = cv2.erode(maske, None, iterations=2)
    maske = cv2.dilate(maske, None, iterations=2)

    # simdi beyaz olan yerlerin etrafini cizdirelim (kontur bulma)
    sinirlar, _ = cv2.findContours(maske.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # eger ekranda yesil bi sey bulduysa iceri girsin
    if len(sinirlar) > 0:
        # en buyuk parcayi al (en buyuk yesil alan)
        en_buyuk_parca = max(sinirlar, key=cv2.contourArea)
        
        # dikdortgen kutu icine alalim
        rect = cv2.minAreaRect(en_buyuk_parca)
        kutu = cv2.boxPoints(rect)
        kutu = np.int64(kutu) # koordinatlari tam sayi yapiyoruz

        # kutuyu cizdir (Yesil renk olsun, kalinlik 2)
        cv2.drawContours(goruntu, [kutu], 0, (0, 255, 0), 2)

        # Yaziyi yazdiralim: Kutu koordinatlarini bulup ustune yazcam
        x, y, w, h = cv2.boundingRect(en_buyuk_parca)
        
        # Buraya istedigimi yazabilirim
        cv2.putText(goruntu, "URUN SAGLAM - ONAYLANDI", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Sonuc ekranini goster
    cv2.imshow('Kalite Kontrol Ekrani - Kaan', goruntu)
    
    # q tusuna basinca kapansin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ram i bosalt
kamera.release()
cv2.destroyAllWindows()