class GrandParent:
    house = "GrandParenthouse"

    def __init__(self, house):
        self.house=house

    def display2(self):
        print("This is GrandParent",self.house)


class Parent:
    house1 = "ParentHouse"

    def __init__(self, house1):
        self.house1=house1

    def display1(self):
        print("This is parent",self.house1)


class child(GrandParent, Parent):

    def __init__(self,house,house1):
        self.house1=house1
        self.house=house
        GrandParent(self.house)
        Parent(self.house1)

    def display(self):
        print("This is child")


obje = child('gp h','p h')
obje.display()
obje.display1()
obje.display2()
