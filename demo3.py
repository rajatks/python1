from demo2 import Person; 
import pickle;
p1=Person("Raju",22);
f1=open("person.ser","wb");
pickle.dump(p1,f1);
f1.close();
print("pickled succesfully ...");
