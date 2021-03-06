# %load q02_data_split/build.py
from greyatomlib.multivariate_regression_project.q01_load_data.build import load_data
from sklearn.model_selection import train_test_split
import pandas as pd
df = load_data('data/student-mat.csv')

# Write your code below
def split_dataset(df):
    
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test= split_dataset(df)
print('shape: ', X_train.shape)
X_train.head()
X_test.head()

