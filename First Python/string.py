website = "http://www.sadikyolcu.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

print(kursAdi)

result = kursAdi
print(result)


print(website[7:10])

c = len(website)
print(c)
print(website[c-3:c])   # İndis ile karakter sayısını karıştırma


k = len(kursAdi)
print(k)

print(kursAdi[-15:])

print(kursAdi[15::2])

print(kursAdi[::-1])

kursAdi = kursAdi.replace("P", "p", 2)  # İlk 2 p harfini değiştir.
# 2'yi silesen tüm p'leri değiştirir.
print(kursAdi)

x = website.replace("w", "W", 1)
print(x)
print()

z = kursAdi.replace("python", "Java", 1)  # count kısmını silersen tüm python'lar degisir.
print(z)

sonuc=kursAdi.split()
print(sonuc)
print()

name, surname, age = 'Mary', 'Drive', 41
print("My name is {} {}.I'm {} years old.".format('Mary', 'Drive', 41))

print(f"My name is {name} {surname}.I'm {age} years old.")

