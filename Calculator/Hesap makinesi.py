sayi1 = int(input( "İlk sayı= "))
sayi2 = int(input( "İkinci sayı= "))

islem =input("""Yapmak istediğiniz işlemi giriniz. 
(+,_,*,/) : """)

if islem=="+" :
    print("Sonuç= "+str(sayi1+sayi2))
elif islem=="-"  and sayi1>sayi2:
    print(sayi1 - sayi2)
elif islem == "-" and sayi2 > sayi1:
    print(sayi2 - sayi1)
elif islem == "*" :
    print(sayi1 * sayi2)
elif islem == "/" :
    print(sayi1 / sayi2)
else:
    print("hatalı deger girdiniz.")
