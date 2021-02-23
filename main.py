import dosyalama1 as Dos
import os
hesapListe=[]
def menu(adres=r"projeBanka\bankaDefter.csv"):
    global hesapListe
    hesapListe=Dos.HesapOlustur(adres)
    menu=f"""
    {"-"*28}
    1-Bakiye Sorgulama
    2-Para Yatırma
    3-Para Çekme
    4-Hesaplar Arası Para Transferi
    5-Çıkış
    {"-"*28}
    """
anahtar = 1
while anahtar==1:
    islem=input(menu)
    if islem:
        if islem in range(1,5):
            if islem==1:
                Dos.bakiyeSorgulama()
            elif islem==2:
                hesapNo=int(input("Para yatırmak istediğiniz hesabı seçiniz."))
                tutar=int(input("Yatırmak istediğiniz tutarı giriniz."))
                Dos.paraYatir(hesapNo,tutar)
                Dos.bakiyeSorgulama()
                        
            elif islem==3:
                hesapNo=int(input("Para çekmek istediğiniz hesabı seçiniz."))
                tutar=int(input("Çekmek istediğiniz tutarı giriniz."))
                Dos.paraCekme(hesapNo,tutar)
                Dos.bakiyeSorgulama()
                       
            elif islem==4:
                hesapNo1=int(input("Para çekmek istediğiniz hesabı seçiniz."))
                hesapNo2=int(input("Para yatırmak istediğiniz hesabı seçiniz."))
                tutar=int(input("Transfer etmek istediğiniz tutarı giriniz."))
                Dos.paraTransferi(hesapNo1,hesapNo2,tutar)
                Dos.bakiyeSorgulama()
                    
            if islem==5:
                anahtar=0
                        
        else:
            print("Geçerli bir işlem numarası giriniz.")
    else:
        print("İşlem numarasını sayısal olarak giriniz.")
else:
    Dos.bankaGunSonu(r"projeBanka\bankaDefter.csv") 
         




menu(r"projeBanka\bankaDefter.csv")
