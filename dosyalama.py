import dosyalama1 as Dos
import os
hesapListe=[]
def DosyaAc(adres,param):
    from os.path import exists
        if param == 1:
            return open(adres,"r+",encoding="UTF-8") 
        elif param == 2:
            return open(adres,"a+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")






def HesapOlustur(adres):
    dosya=DosyaAc(adres,1)
    if len(dosya.read()):
        dosya.seek(0)
        liste=dosya.readlines()
    else:
        liste=[]
        for i in range(1,3):
            liste.append(";".join((f"Hesap{i}","0"))+"\n")
        else:
            dosya.seek(0)
            dosya.writelines(liste)
        dosya.close()
    return liste
hesapListe=HesapOlustur(r"projeBanka\bankaDefter.csv")
if __name__== "__main__":
    hesapListe=HesapOlustur(r"projeBanka\bankaDefter.csv")

def bakiyeSorgulama():
    global hesapListe
    sonuc ="BAKİYENİZ\n"
    for item in hesapListe:
        sonuc += f"""{item.split(";")[0]} Bakiyeniz (TL):{item.split(";")[1]}"""
    print(sonuc)


def paraYatir(hesapNo=0,tutar=0):
    global hesapListe
    hesap=hesapListe[hesapNo].split(";")
    hesap[1]=((float(hesap[1].replace("\n",""))+tutar))   
    print(hesapListe)
    hesapListe[hesapNo]=";".join(hesap)+ "\n"
    print(hesapListe)

def paraCekme(hesapNo=0,tutar=0):
    global hesapListe
    hesap=hesapListe[hesapNo].split(";")
    bakiye=(float(hesap[1].replace("\n","")))
    if bakiye>=tutar:
        hesap[1]=(str(bakiye-tutar))
    else:
       Mesaj("Yetersiz Bakiye",1)
    hesapListe[hesapNo]=";".join(hesap)+ "\n"
    print(hesapListe)

def bakiyeKontrol(hesapNo=0,tutar=0):
    global hesapListe
    hesap=hesapListe[hesapNo].split(";")
    bakiye=(float(hesap[1].replace("\n","")))
    if bakiye>=tutar:
        return True
    else:
        return False

def paraTransferi(Hesap1=0,Hesap2=1,tutar=0):
    global hesapListe
    if bakiyeKontrol(Hesap1,tutar):
        paraCekme(Hesap1,tutar)
        paraYatir(Hesap2,tutar)
    else:
        Mesaj("Yetersiz Bakiye",1)

def Mesaj(mesaj,tip):
    mesajtipi = ""
    if tip == 1:
        mesajtipi = "!"
    elif tip == 2:
        mesajtipi = "?"
    elif tip ==3 :
        mesajtipi = "*"
    mesajtipi *= 20 
    print(mesajtipi,mesaj,mesajtipi)



def bankaGunSonu(adres):
    global hesapListe
    dosya=DosyaAc(adres,1)
    dosya.truncate()
    dosya.writelines(hesapListe)
    dosya.close()
