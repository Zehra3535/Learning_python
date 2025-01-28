
mes='hello world\n'

print(mes.count('l')) #cümlede kaç kere geçtiğini buluyor
print(mes.count('world'))

print(mes)

new_mes=mes.replace('world','universe')
print(new_mes)

greeting='Hello'
name='Sinan'
message=greeting +' '+ name+'! Welcome.'
print(message)
message= '{} ,{}. Welcome!'.format(greeting,name)
print(message)


color='red'
thing="chair"

text="{} is {} .You know...".format(thing,color)
print(text)

text= f'{thing.capitalize()} was {color}.You know...\n'
print(text)  #capitalize :İlk harfi büyütür.

#print(dir(thing))  #Kullanabileceğimiz fonksiyonları gösterir.

#print(help(str)) #Fonksiyonların nasıl kullanıldığını gösterir.

#print(help(str.lower)) #lower fonksiyonu nasıl kullanılır.
print('\n')


my_list = ['x','y','z']
ur_list = ['r','s']

my_list.append('q')
print(my_list)

print(len(my_list))

print(my_list[:2]) # 1:3 sonra 1: yaz.
print(my_list[-1]) # Son elemanı gösterir.Parametreye 0 sonra -2 yaz.
print('\n')

ur_list.insert(2,'t')
print(ur_list) #-1. indexte ne olduğuna bak. (40.satır)

my_list.remove('q')
print(my_list)


print(my_list.index('z'))
print('\naşağıda')

#my_list.insert(0,ur_list)
#print(my_list)

my_list.extend(ur_list)  #extend:devam ettirmek
print(my_list)

#my_list.append(ur_list)  #append: eklemek, iliştirmek
#print(my_list)

popped=my_list.pop()
print("popped element is = " + popped)
print(my_list)

for nesne in my_list:
    print(nesne)
print('\n')

for index,nesne in enumerate(my_list):
    print(index,nesne)
    print('\n')
for index,nesne in enumerate(my_list,start=1):
    print(index,nesne)

my_list.reverse()
print(my_list)

print("\n")

my_list.sort() #alfabetik olarak sıraladı.
print(my_list)
nums=[7,4,9,8,2,99]
#nums.sort()   # Küçükten büyüğe sıralar.
#nums.sort(reverse=True)  # Büyükten küçüğe sıralar.
sort_function=sorted(nums) #geçici değişken yaptık.orijinal nums değişmedi.
print(sort_function)
print(nums)

print("\n")

print(74 in nums)
print('y' in my_list)

print('\n')
# Creating a Multi-Dimensional List
List = [['Hey', 'For'], ['Geeks']]
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
List.insert([1][0],'hiyeee')
print(List)