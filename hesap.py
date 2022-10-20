import math
hesap_menu = """
[+]Toplama Yapmak için
[-]Çıkarma Yapmak için
[*]Çarpma yapmak için
[/]Bölme yapmak için
[5]üst almak için
[6]Kare kök almak için
[7]Bölenden kalan bulmak için
[Q]Çıkış yapmak için
"""
def topla(a,b):
    sonuc=0
    sonuc = a+b
    print("toplamın sonucu :",sonuc)
def cikarma(a,b):
    sonuc=0
    sonuc = a-b
    print("çıkarma sonucu :",sonuc)
def carpma(a,b):
    sonuc=1
    sonuc = a * b
    print("çarpma işlemi sonucu :",sonuc)
def bolme(a,b):
    sonuc=1
    try:
        print("bölme işleminin sonucu :",float(a/b))
    except ZeroDivisionError:
        print("0' a bölüm tanımsızdır :")
def üsalma(a,b):
    sonuc=1
    sonuc = a**b
    print("üs alma işlemi sonucu :",sonuc)
def kökalma(a):
    print("Sayının Kökü : ",int(math.sqrt(a)))
def kalan_bulma(a,b):
    sonuc=a%b
    sonuc1=int(a/b)
    print(a,"'in ",b,"bölüm sonucu :","bölüm :",sonuc1," kalan : ",sonuc)
while True:
    print(30*"==",hesap_menu)
    secim =input("Yapıcağınız işlemi menüden seçiniz")
    if secim=="+":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        topla(a,b)
    elif secim=="-":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        cikarma(a,b)
    elif secim=="*":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        carpma(a,b)
    elif secim=="/":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        bolme(a,b)
    elif secim=="5":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        üsalma(a,b)
    elif secim=="6":
        a = int(input("bir sayi giriniz :"))
        kökalma(a)
    elif secim=="7":
        a = int(input("bir sayi giriniz :"))
        b = int(input("bir sayi giriniz :"))
        kalan_bulma(a,b)
    elif secim=="q" or secim=="Q":
        quit()