import pickle;
from demo2 import Person;
f2=open("person.ser","rb");
p1=pickle.load(f2);
#print(p1);
print(p1.name);
print(p1.age);
