human=False
print("are you human?= "+str(human))

name= "Clara"
surname= "Stan"
print( name + " " + surname )

age=20
age+=1
print("\nYOU'RE AGE =" + str(age) )

#lunapark
gondol = True
if gondol:
    print("\nEnes gondola binecek.")
elif not gondol:
    print("gondolsuz lunapark mı olur ")
else:
    print("çıkış")

nu1,nu2,nu3 ="\nsıkıldım",0 ,True
print(nu1 ,nu2,nu3)
print(nu2)
print(nu3)
print("\n")

variable="HiPythonn"
print(variable)
print(variable.isdigit())   # Rakamlardan mı oluşuyor?
print(variable.isalpha())  #Are these alphabetic characters?Don't put space in sentence
print(variable.count("n"))  #kaç tane 'n' var?
print(variable.replace("n","ğ"))  # n yerine ğ koyduk.
print(variable*3)
print("\n")

      #01234567
name= "Bro Code"
a1 = name[2]
print(a1)

a2 = name[0:3] # ==name[:3]
#First index is inclusive, the stopping index is exclusive.
print(a2)

a3 = name[4:8] # ==name[4:]
print(a3)

reversed_name=name[::-1]
print(reversed_name) # reverse=tersine çevirmek

        #012345678       -54321-
website="https://www.google.com"
website2 = "https://www.wikipedia.org/"

slice = slice(8,-4)
print(website[slice])
print(website2[slice])
