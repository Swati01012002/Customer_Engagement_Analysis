import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')
df.head()
df.info()
df.describe() #to get summary statistics of numerical columns
df.describe(include='all') #to get summary statistics of all the columns
df.isnull().sum()
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())