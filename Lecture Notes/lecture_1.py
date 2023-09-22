# sayilar=[1,2,3,4,5,6,7,8,9]
# sayilarEkleme=[1,2,3,4]
# sayilar.append(100)

# print(sayilar.pop())
# print(sayilar.remove(5))
# print(sayilar)
# print(sayilar[-1])
# sayilar.extend(sayilarEkleme)
# print(sayilar)

# sayilar.append(sayilarEkleme)
# print(sayilar)

# sayilar.clear()
# print(sayilar)



# ------------------------------KOŞULLAR-------------------------------------



# ortalamaNot = input("Sayı gir: ")
# ortalamaNotAsInteger = int(ortalamaNot)

# if ortalamaNotAsInteger > 50:
#     print("Bravo")
# elif ortalamaNotAsInteger<40:
#     print("Başarısız")
# else:
#     print("kaldınız")

# print("bağımsız çalışacak kısım")



# ------------------------------DÖNGÜLER-------------------------------------


#For:

# enBuyuk=0
# for i in range(0,10):
#     sayi = int(input(f"{i+1}.Sayı gir: "))
#     if sayi>enBuyuk:
#         enBuyuk =sayi

# print(f"en büyük: {enBuyuk}")


# sayilar =[]

# for i in range(3):
#     sayilar.append(input(f"{i+1}.Sayı gir: "))

# sayilar.sort()
# enbuyuk = int(input("en buyuk hangisini istersin: "))
# print(sayilar[-1])



#While:

# i=0
# while i<10:
#     print(i)
#     i=i+1
    



# ------------------------------FONKSİYONLAR-------------------------------------


# def ortalamaHesapla() -> float:
#     final=80
#     vize=59

#     ortalama = (vize*0.4+final*0.6)
#     return ortalama


# #fonksiyon dışına çıkıyoruz
# print(ortalamaHesapla())


# def ortalamaHesapla(vize: float, final: float) -> float:
#     return (vize*0.4+final*0.6)

# print(ortalamaHesapla(85,45))