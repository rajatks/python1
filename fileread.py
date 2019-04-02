import pandas as pd;

emp=pd.read_csv("prodata.csv");
#print(df);

print("min Age : ",emp['age'].idxmax());
print("Max Age : ",emp['age'].idxmin());



