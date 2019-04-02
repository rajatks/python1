class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __str__(self):
        print("Name is : ",self.name);
        print("Age is :  ",self.age);
        return " ";
