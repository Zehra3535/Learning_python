phones = ["S5", "S6", "S7", "S8"]
print(len(phones))

#  phones[0] = "S9"

#  phones[-1] = "S9"
#  phones[-2] = "S10"
phones[-2:] = ["S9", "S10"]  # updates the last 2 element
print(phones)

#  phones.append("I1")
phones.append("I2")
print(phones)
# phones = phones + ["I1", "I2"]


#  phones.remove(phones[-1])
del phones[-1]
print(phones)

#  phones.reverse()
phones = phones[::-1]

print(phones)
#  for x in phones:
#    print(x)
print()


ogrenciA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
ogrenciB = ["Sena", "Turan", 1999, [80, 80, 70]]
ogrenciC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

ogrenciler = [ogrenciA, ogrenciB, ogrenciC]

#  for ogrenci in ogrenciler:
#      print(f"{ogrenci[0]}  {2025-ogrenci[2]}  {ogrenci[3][0]} ")

for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2025-ogrenci[2]
    average = (ogrenci[3][0]+ogrenci[3][1]+ogrenci[3][2]) / 3
    print(f"{ad} {soyad} {yas} {int(average)} ")

