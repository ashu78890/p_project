from abc import ABC, abstractmethod

a = (1, 2, [3, 4])
a[2][0] = 100
print(a)

#a[2] at 0 index this means 3 will replace by 100 and we cannot change list but we can change if there is mutable type is there than we can change that 


x = (1, 2, 3)  
y = x  
x += (4, 5)  
print(x)  
print(y)  


# list1 = [[1, 2], (3, 4)]  # One mutable (list), one immutable (tuple)
# list2 = copy.deepcopy(list1)

# list2[0][0] = 100 
# list2[1] = (100, 200)  #

# print(list1)  # ???
# print(list2)  # 



class Food(ABC) :
 def __init__(self):
   self.__sweet = "Rabdi"
    
 def type(self):
        print("indian")

 def get_sweet(self):
        return self.__sweet 



class Thai(Food):
    def type(self):
        print("english breakfast")

    def get_sweet(self):
        return super().get_sweet()

getfood = Food()
getthai = Thai()
print(getfood.type())
print(getthai.get_sweet())



