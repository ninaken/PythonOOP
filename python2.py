import csv
class Calculator:
     def __init__(self,a,b):
        self.a=a
        self.b=b

     def  plus(self):
        return self.a+self.b

     def minus(self):
        if self.a>self.b:
           return self.a-self.b
        else:
            return self.b-self.a
     def gayopa(self):
        return self.a/self.b
     def mult(self):
        return self.a*self.b
      
     def info(self):
        return f"Plus:{self.plus()}, Minus:{self.minus()}, Gayopa:{self.gayopa()}, multiplication:{self.mult()}"


      
b=Calculator(5,4)
print(b.plus())
print(b.minus())
print(b.info())

class Rectangle():
   def __init__(self, width,length):
      self.width=width
      self.length=length

   def area(self):
      return self.width*self.length
   
   def perimeter(self):
      return self.width+self.length
   def printinfo(self):
      return f"Area:{self.area()}, Perimeter:{self.perimeter()}"



c=Rectangle(2,3)
print(c.area())
print(c.printinfo())


class Employee():
   def __init__(self, name, surname,age, salary):
      
      self.name=name
      self.surname=surname
      self.age=age
      self.salary=salary
   
 
   def minimalsalary(self):
      minimal=None
      for i in self.salary:
         if not minimal or i>minimal:
            minimal=i
            return i


def databse():
 with open("dataset1.csv", "r") as csv_file:
    csvreader=csv.reader(csv_file)
    count=0
    for row in csvreader:
       return row

c=Employee(databse())
print(c.minimalsalary())
