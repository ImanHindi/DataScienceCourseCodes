from matplotlib.pyplot import plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

D={'one':pd.Series([1,2,3],index=['A','B','C']),
    'two':pd.Series([1,2,3,4],index=['A','B','C','D'])}


df=pd.DataFrame(D)

print(df['one'])

df['Three']=pd.Series([1,2,3,4],index=['A','B','C','D'])
df['Four']=df['one']+df['Three']

print(df.Four)

x=df.pop('Four')
print(df)

df['Four']=x
print(df)

#del df['Three']
#print(df)
#select a row and return it as series with label of the row index..
print(df.loc['A'])
print(df.iloc[0])

print(df[0:1])

#add rows:

df=df.append(df)
print(df)
print(df[0:5])
print(df.iloc[6])
print(df.loc['A','one'])
print(df.loc[:,['one','two']])

#delete row:

print(df.drop('A'))
print(df)
df.drop(['Four'], axis=1)
df.T


print(df.dtypes)
print(df.empty)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values[0])
print(df.values)#return data as numpy arrays of 2 dimentions
print(df.tail(1))
print(df.head(2))
print(df.describe())
print(df.apply(np.mean,axis=1))
df.iteritems()#iter for colum and all the values under it (key ,values)pair (column name,series)
df.iterrows()#Iterates over datafram rows as (index,series)
df.itertuples()#return a tuple of each row and vlues related to it in each coloum


#for key,values in df.iteritems():
#    print(key)
#    print(values)



#for row,s in df.iterrows():
#    print(row)
#    print(s)


#for row in df.itertuples():
#    print(row[:4])

print(df)
#DROP FUNCTION:

#drop is not affected the original data fram 
#return a new df that can be stored in anew df
#print(df.drop(['Four','Three'], axis=1))
#print(df.drop(['B','C'], axis=0))
#print(df)

#affected the original df drop columns of index 0 ,1,3
#print(df.drop(df.columns[[0, 1, 3]], axis = 1, inplace = True))
#print(df)


#affected the original df
#drop rows A and B and columns one and Four
#print(df.drop(index=['A','B'], columns=['one','Four'], inplace = True))
#print(df)


# Remove all columns between column index 1 to 3
#affected the original return df after droping colums
#print(df.drop(df.iloc[:, 1:3], inplace = True, axis = 1))
#print(df)



# Remove all columns between column name 'one' to 'Three'
#not affect the original df 
# drop colums and return df after droping colums
#print(df.drop(df.loc[:, 'one':'Three'].columns, axis = 1))
#print(df)


#Drop Rows in a DataFrame with conditions
#print(df.drop(df[df['Four'] < 6].index))
#print(df)

#APPLY FUNCTION
#df.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)

#axis=0 iterate over rows in one cloumn
#print(df.apply(np.sum, axis=0))
#iterate over coloumns in one row
#print(df.apply(np.sum, axis=1))


#print(df.apply(lambda x: [1, 2], axis=1))
#print(df.apply(lambda Value : Value * 10))


#print(df['Four'].dtype)
#print(df['Four'].astype(float))
#print(df['Four'].dtype)

#df=df.replace(['Nan'],0)
#print(df)
#print(df.dropna(subset=['one']))
#
#print(df['Four'].dropna(inplace=True))
#
#print(df)

#print(df['Four'].fillna(value=df['Four'].mean()))
print(df.query('Four>3'))
#print(df)

print(df[df['Four'] >3])


#df=df.reset_index()
print(df)


df=df.reindex()
print(df)

#group by....

# Use GroupBy() & compute sum on specific column
df2 = df.groupby('Four')['one'].sum()
print(df2)


df2.plot.bar(y=df.columns[0])
plt.show()
