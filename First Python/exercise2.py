def say_hi(name,number):
    print("Hi "+name+str(number))

print("Welcome")
say_hi("Jim",1)


def cube(num):
    return num*num*num  #The return keyword terminates the execution of a function.
    print("code")  #In functions, the code after the return statement is not executed.

print(cube(4))

is_female= False
is_tall= True

if is_female and is_tall:
    print("You're tall female.")
elif is_female and not is_tall:
    print("You are short female.")
elif not is_female and is_tall:
    print("You are tall male.")
else:
    print("You're not tall and not female")

def max_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>a and b>=c:
        return b
    else:
        return c

print(max_num(57,13,21))
print(max_num(a=5,b=40,c=0))
