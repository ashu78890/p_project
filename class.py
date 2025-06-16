class  Employee:
    name = "ashish"    #class attribute
    rollno="1223"
    def root(self,name,rollno):
        print(self.name,self.rollno)
    def root1():
        print()
    def __init__(self):  #in it is dunder method it will call automaticlly if we create any object 
        print("methisi")  

z = Employee()  #this is object
z.age= 23
z.name ="sham"   #instance attribute  / will always prfer this first 
print(z.name,z.rollno,z.age)
# z.root()

class programer :
    comapanyName="microsoft"
    def __init__(self,name,salary):
        self.name =name,
        self.salary =salary 

data = programer("nothch", 25555)
print(data.comapanyName,data.name,data.salary)     


class caluclator:
    def __init__(self,n):
        print(n*n,n*n*n,)
caluclator1 = caluclator(9)






#inheritance 
class company :
    net_worth = 4000
    # def companynmae():
    #  print("choudhary & sons")

class salary :
    salary_person=433

    def __init__ (self):
       print ("ashish choudhary")
  
class employee(company,salary) :
    print("ashish choudhary")

a = employee()
print(a.net_worth,a.salary_person)
# company.companynmae()
print(a.net_worth,a.salary_person)
