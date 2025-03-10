
# ashish

# a =int(input("hi add 1st number :"))
# b =int(input("hi add 2nd number :"))

# print(a+b)
a ="Ashishshfjhsdgfh"
print(a)
shortname = a[0:2] 
shortname = a[-2:-1]
shortname= a[1:2] 
# shortname =a[0::3]

print(shortname)
print(len(a))


my_list = [1,2,3,3,3,5]

print(my_list.append(2))
print(my_list)    


z = ()
print(type(z))


# fruits = input("enter fruit name ")

data={
"lots":"hattu",
 "harry":90
}

print(data.items())
print(data.update({"nod":33}))
print(data)


jab =set()
print(type(jab))
# print(jab([2,34,34,2,2,21]))
print(jab.add(334))
print(jab)

j =10
if(j>20):
    print("true hai")
elif(j==9):
    print("true ha")
elif(j ==10 or j>5):
    print("true tha")


    
for i in range(100):
    if (i==2):
        continue
print(i)

for i in range(1,8):
    if(i==4):
        continue
print(i)

i = [1,2,3,4,5,6,7,8,9]

for item in i:
    if(item < 3):
        print(item)
        continue
print(item)

# i = [1,2,3,4,5,6,7,8,9]
# while(item in<3):
#     print(i)
#     break

# i = ["asg","ffg","ssd"]

# for item in i:
#     if(item.startswith("s")):
#         print(item)
# i = 0

# number = int (input("write a number"))
# i = 0
# for i in range(1,number+1):
#     if not(i%2 == 0):
#      print("*"*i)


def function_1(n):
    print(n)

function_1("daoya")

def function_1(n):
    if(n==0 or n==1):
        return 1
    z = n * function_1(n-1)
    return z
print(function_1(10))



# x = (1, 2, 3)
# y = x
# y += (4,)
# print(x)
# print(y)

x = [[1, 2], [3, 4]]
y = x[:]
x[0].append(99)

print(y)
