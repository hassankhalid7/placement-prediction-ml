import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("placement (1).csv")   # Put the correct path

# Show first 5 rows
print(df.head())

df.head()
df.info()
df.shape
df.head()

df= df.iloc[:,1:]
plt.scatter(df['cgpa'],df['iq'],c=df['placement'])


X = df.iloc[:,0:2]
y = df.iloc[:,-1]
     

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)

print(X_test)
print(y_train)