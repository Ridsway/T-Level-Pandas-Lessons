print("step 1")
print("import the libraries you will need")
import pandas as pd

print("step 2")
print("get the dataset")
print("step 3")
print("save it to a sensible variable name")
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')

print("step 4")
print("look at the first 25 entries")
input()

#Your code goes here:

print("#"*10)
print(df.head(25))

print("step 5")
print("look at the last 10 entries")
input()

#Your code goes here:

print("#"*10)
print(df.tail(10))
input()

print("step 6")
print("find out the number of rows in the dataset")

#Your code goes here:

print("#"*10)
print(df.count)
input()

print("step 7")
print("found out the number of columns in the dataset")

#Your code goes here:

print("#"*10)
print(df.count)
input()

print("step 8")
print("print the names of all the columns")

#Your code goes here:

print("#"*10)
print(df.columns)
input()

print("step 9")
print("find out how the data is indexed (what are the labels)")
print(df.index)

#Your code goes here:

print("#"*10)
input()

print("step 10")
print("what are the data types of each column")

#Your code goes here:

print("#"*10)
print(df.dtypes)
input()

print("step 11")
print("print only the 'occupation' column")

#Your code goes here:

print("#"*10)
print(df.occupation)
input()

print("step 12")
print("find out how many different occupations are in this dataset")

#Your code goes here:

print("#"*10)
print(df["occupation"].value_counts())
input()

print("step 13")
print("what is the most frequent occupation")

#Your code goes here:

print("#"*10)
occupationNo = (df["occupation"].value_counts())
print(occupationNo.head(1))
input()

print("step 14")
print("summarize the dataFrame")

#Your code goes here:

print("#"*10)
print(df.info())
input()

print("step 15")
print("summarize every column in the dataFrame")

#Your code goes here:

print("#"*10)
print(df.describe(include="all"))
input()

print("step 16")
print("summarize only the occupation column")

#Your code goes here:

print("#"*10)
print(df["occupation"].describe(include="all"))
input()

print("step 17")
print("what is the mean age of all the users")

#Your code goes here:

print("#"*10)
print(df["age"].mean())
input()

print("step 18")
print("what is the least frequent occupation")

#Your code goes here:

print("#"*10)
print(occupationNo.tail(1))
input()

