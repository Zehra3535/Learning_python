msg = "Welcome to our school.".split()
print(msg)
print(msg[0])
print(msg[0][0])


greet = "Hi people."
print(greet[0])


Lg = ["Python", "Java", "C#", "React", "Javascript"]
print(type(Lg))
print(Lg[1:3])
print(Lg[-3:-1])
Lg[-1] = "Html"

if "Python" in Lg:
    print("The value is in the list")

for x in Lg:
    print(x)


print()
newList = Lg + ["Angular", "Vuejs"]
print(newList)

print()
del Lg[2]  #Deletes the element at the 2. index
print(Lg)
