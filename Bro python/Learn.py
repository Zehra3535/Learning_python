kitap_ismi= "moby dick"
sayfa_sayisi=195
agirlik=13.45
yeni_mi=True

print(kitap_ismi)
print(sayfa_sayisi)
print(agirlik)
print(yeni_mi)
print('\n')
mes='hello world\n'
print(mes.count('l')) #cümlede kaç kere geçtiğini buluyor
print(mes.count('world'))
print(mes)
new_mes=mes.replace('world','universe')
print(new_mes)


zenci=type(yeni_mi)
print(zenci)

print( type(agirlik))

#kim=input("kimin adı? = ")
#print("Çok memnun oldum.Ben "+kim)

#alan=input("\nHangi alanda çalışmak istiyorsun? = ")
#dil=input("Hangi programlama dili? = ")
#print(alan+" için "+dil+ " öğrenmeliyim. ")

#sayi1= input("İlk sayı= ")
#sayi2= input("İkinci sayı= ")
#print=(sayi1+sayi2)
#print(int(sayi1)+int(sayi2))

#mutlak değer
print(abs(-9.7))

#mat kütüphanesi ekleyelim
import math
print(math.sqrt(49) )
print(min(3,70,1,9))
print(max(2,6,1,48))
print("\n")

pi=3.14
print(pi.__round__())
print(pi.__ceil__()) #ceil=tavan
print(pi.__floor__()) #floor=taban
print(abs(pi))  #absolute= mutlak
print(pow(pi,2)) #üs
print(math.sqrt(81) )



print("\n")

       #0123456789...
news="""all’s fair in love and poetry... 
New album THE TORTURED POETS DEPARTMENT"""
                            #...7654321
print(news)
print(news[0])
print(news[6])
print(news[0:4]) # 0 dahil ama 4 dahil değil.ilk sınır dahil ikinci sınır dahil değil.
print(news[-1]) #son harf
print(news[-7:-1]) #-7 dahil ,-1 dahil değil.
print(news[-2:-1])


print(len(news))   #length function

print(news.lower()) #all letters are lowercase

print(news.title()) #first letter is BİG
print("\nsmile\n")
BIG="all letters are uppercase."
print(BIG.upper())
print( BIG.find("a"))
print( BIG.find("e"))
print( BIG.find("x")) #Since there is no x in the text, -1 is returned.

cumle="tatlı elma nerede?"
print(cumle.replace("elma","kiraz"))

#ad =input("Adını gir= ")
#print("adınız= "+ad.title())

mutlu = True
zeki = False

if mutlu and zeki:
    print("MÜKEMMEL")
elif mutlu and not zeki:
    print("Saaade küfte(mutlu):) ")
elif mutlu or zeki:
    print("Bir VARMIŞ Bir Y0KMUŞ.")
else:
    print("Abe napak. Sicaktırr ")

yas=int(input("KAç yaşındasın? = "))
okulBitti=input("Okuyon mu?=(True:t False:f) ")

if yas>18 and okulBitti=="t":
    print("Hadi askere ")
elif yas>18 and okulBitti=="f":
    print("Hadi okula ")
else:
    print("Askerlik yaşın gelmedi..")

input("\nEnter your age? =  ")