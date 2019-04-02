import pandas as pd;
import numpy as np;

data=np.array(['rakesh','mahesh','suman','ankit','saurabh']);
s=pd.Series(data,index=[101,102,103,104,105]);
print(s);
print("----------------");

s=pd.Series('hello',index=[100,102,103,105]);
print(s);
print("-----");

