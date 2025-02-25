friends= ["Kelly","Karen","Jack","Toby","Kelly","Kelly"]
friends.insert(1,"Mike")
friends.remove("Jack")
print(friends)
#friends.pop(2)
#friends.clear()  #deletes all the elements
print(friends)
#friends.pop() #removes last element
print(friends.index("Toby"))
print(friends.count("Kelly")) #How many Kelly

friends.sort()  #ascending order
print(friends)
friends.reverse()  #descending order
print(friends)

friends2=friends.copy()
print(friends2)