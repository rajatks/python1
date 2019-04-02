class Emp:
    def __init__(self,name,salary,age):
        self.name=name;
        self.salary=salary;
        self.age=age;
    def __str__(self):
        print("Name : ",self.name);
        print("Salary : ",self.salary);
        print("Age : ",self.age);
        return " ";
    def __add__(obj1,obj2):
        x=obj1.salary;
        y=obj2.salary;
        z=x+y;
        e=Emp("Mr Verma Family :",33,z);
        return e;
    def __gt__(obj1,obj2):
        x1=obj1.age;
        y1=obj2.age;
        if(x1>y1):
            return True;
        else:
            return False;
        
            

e1=Emp("rashi Verma",32000,32);
e2=Emp("Sushil Verma",50000,21);
e3=Emp("Akash Verma",25000,41);

print(e1);
print(e2);
print(e3);

e4=e1+e2+e3;
print(e4);

if e1>e3:
    print("Mr "+e1.name+" is greater than "+e3.name);
else:
    print("Mr "+e3.name+" is greater than "+e1.name);


       
