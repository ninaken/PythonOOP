#1



class Book:
    def __init__(self, bookname, author, publyear,pagecount):
        self.__bookname=bookname
        self.__author=author
        self.__publyear=publyear
        self.__pagecount=pagecount

    def get__bookname(self):
        return self.__bookname

    def set__bookname(self, bookname):
        self.__bookname=bookname

    def get__author(self):
        return self.__author

    def set__author(self, author):
        self.__author=author

    def get__publyear(self):
        return self.__publyear

    def set__publyear(self, publyear):
        self.__publyear=publyear

    def get__pagecount(self):
        return self.__pagecount

    def set__pagecount(self, pagecount):
        self.__pagecount=pagecount

    def printinfo(self):
        return f"წიგნი:{self.__bookname}, ავთორი:{self.__author}, გამოშვების წელი:{self.__publyear}, გვერდების რაოდენობა:{self.__pagecount}"



d=Book("EvgeniyOnegin", "Pushkin", 1712, 90)
print(d.printinfo())
#2
class Biblio(list):
    def __init__(self,listi):
        self.listi=listi
    def min1(self):
        k=min(self.listi)
        return k

    def max2(self):
        d=max(self.listi)
        return d

    def printinfo(self):
        return f"მაქსიმუმი:{self.min1()},მინიმუმი:{self.max2()}"

listi=[45,45,343,11]
d=Biblio(listi)
print(d.printinfo())

#3
class Animal():
    def __init__(self, name, age):
        super().__init__()
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name=name

    def get_name(self):
        return self.__age
    def set_name(self, age):
        self.__age=age

    def printinfo(self):
        return f"ცხოველი:{self.__name}, ასაკი:{self.__age}"


class Dog(Animal):
    def __init__(self, name, age,jishi, colour):
        super().__init__(name,age)
        self.__jishi=jishi
        self.__colour=colour
    def get_jishi(self):
        return self.__jishi
    def set_jishi(self,jishi):
        self.__jishi=jishi
    def get_colour(self):
        return self.__colour
    def set_colour(self, colour):
        self.__colour=colour
    def printinfo1(self):
        return Animal.printinfo(self)+f"ჯიში:{self.__jishi}, ფერი:{self.__colour}"


pet=Dog("bobi","4","dalmatinec","black")
print(pet.printinfo1())

#4
class CallMixin():
    def call(self, number):
        print("calling to"+number)



class Person():
    def __init__(self, fname, lname, phone):
        self.fname=fname
        self.lname=lname
        self.phone=phone


class Call(Person, CallMixin):
    pass

caller=Call("khasaia", "nina", "82829920202")
print(caller.call("588585949"))
print(caller.info())








    




    
