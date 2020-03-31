import os
import time
asılkitaplistesi=list()
menu = (""""
Kütüphane uygulamasına hoşgeldiniz yapmak istediğiniz işlemi seçiniz:
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[4] Çıkış
""")
def kitapekle(kitap:str,kitapliste:list):
    sayac = 0
    for i in kitapliste:
        if i == kitap:
            sayac+=1
    if sayac == 1:
        print("Eklenmedi!. Kitap listenizde bulunmaktadır.")
        print("Ana menüye Dönmek için Enter'a basın")
        input()
    else:
        kitapliste.append(kitap)
        print("Başarılı! ",kitap," kitap listesine eklendi.")
        print("Ana menüye Dönmek için Enter'a basın")
        input()

def kitapal(kitap:str,kitapliste:list):
    sayac=0
    for i in kitapliste:
        if i==kitap:
            sayac=sayac+1
    if sayac==1:
        kitapliste.remove(kitap)
        print("Başarılı! Kitap sizin için ayırtıldı.\nAna menüye dönmek için Enter'e basın.")
        input()
    else:
        print("Girdiğiniz kitap ismi listemizdeki kitaplar ile uyuşmuyor.\nLütfen tekrar denemek için Enter'a basın.")
        input()

def kitaplistele(kitapliste:list):
    sayac=0
    for i in kitapliste:
        sayac+=1
        print(sayac,"- Kitap = ",i)
    if sayac == 0:
        print("Henüz bir kitap kaydedilmemiş.")
    print("Ana menüye dönmek için Enter'a basın")
    input()

while True :
    os.system("cls")
    print(menu)
    secim=input("Seçiminiz : ")
    if secim=="1":
        kitapgir=str(input("Eklemek istediğiniz kitabı yazınız:"))
        kitapekle(kitapgir,asılkitaplistesi)
        continue
    elif secim=="2":
        kitap =str(input("Almak istediğiniz kitabın ismini yazınız:"))

        kitapal(kitap,asılkitaplistesi)
        continue

    elif secim =="3":
        kitaplistele(asılkitaplistesi)
        continue
    elif secim =="4":
        print("Çıkışınız gerçekleştiriliyor...")
        time.sleep(1)
        print("Çıkışınız Gerçekleştirildi!")
        break
    else:
        print("Hatalı değer girdiniz. Lütfen tekrar deneyin")
        print("Ana menüye dönmek için Enter'a basın")
        input()
        continue