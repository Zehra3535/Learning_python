'''
ad = input("Enter your name= ") #input her zaman string bir değer getirir.tam sayı girmek istersen int() parantezin içine input kısmının yazmalısın
print("Your name is "+ ad )
'''

name="Ken"
surname="Cort"
full_name = name + ' ' + surname
print(full_name)

product1= 50
product2= 60.5
product3 =356.56
total= product1 +product2 +product3
print( "Total price", total )

'''
num1= int(input("enter first num= "))
num2= int(input("enter second num= "))
print("Result =", num1+num2 )
'''

isStudent = True
print(isStudent)

#float to int
money=45.27
outcome=int(money)
print(outcome)

#int to float
age=17
f_age= float(age)
print(f_age)

''' 
pi=3.14
r=int( input("r yi gir: "))
cevre = 2*pi*r
alan = pi * ( r ** 2)
print("Çevre :" + str(cevre) + " Alan :" + str(alan) )
'''
km=float(input("km değerini yaz= "))
mil=km/1.609344
print(mil)