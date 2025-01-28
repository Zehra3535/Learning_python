import time

rows= int(input("How many rows?= "))
columns =int(input("How many columns?= "))
symbol= input("Enter a symbol to use= ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print("")

print("\n")




for i in range(3):
    print(i)
print("\n")

for index in range(13,17):
    print(index)
print("\n")

for index in range(13+1,17):
    print(index)
print("\n")

for index in range(13,17+1):
    print(index)
print("\n")

for j in range(30,50,3):
    print(j)
print("\n")

for i in "Bro Code ":
    print(i)

#import time ekledik yukarıya
for second in range(10,0,-1):
    print(second)
time.sleep(3)
print("Happy new year! \n\n")

name= ""
while len(name) == 0:
    name=input("Enter ur name= ")
print("Hi "+name)



# Logical operators (and, or, not) =used to check if 2 or
# more conditional statements is true

temp=int(input("What is the weather like today in degrees Celsius? = "))

if not( 0 <=temp and temp<=30) :
    print("The temperature is bad. Stay inside!")
elif (temp==20 or temp==25) :
    print("The temperature is optimum")
elif  0 <=temp  and temp <= 30:
    print("The temperature is good.")


name= ""
while len(name) == 0:
    name=input("Enter ur name= ")
print("Hi "+name)
