import pandas as pd
import numpy as np

print("a series is like one column in a table.")
print("if you open an excel document, everything in the column") 
print("labelled A at the top is like a series")

print("each column with a different letter value is like a separate series")

mySeries = pd.Series(
    np.random.randn(5),
    index = ["a","b","c","d","e"],
    name = "example")

print("this series has three parts")
print("1 - the data")
print("   in this series, the data is 5 random values")

print("2 - the index")
print("   in this series, the index is a list of letters from 'a' to 'e'")

print("3 - the name")
print("   in this series, the name is 'example'\n")

print(mySeries)
print("#"*10)
input()

print("you can get the 1st element in a series like you would in a list\n") # 1st element
print(mySeries.iloc[0])
print("#"*10)
input()

print("you can also get every element from the 1st element to the 3rd\n") # 1st to 3rd element
print(mySeries.iloc[:3])
print("#"*10)
input()

print("you can get just the elements at index 4, 3 and 1\n") # specific elements
print(mySeries.iloc[[4,3,1]])
print("#"*10)
input()

print("you can get all of the values in the series\n")  # all values in series
print(mySeries.values)
print("#"*10)
input()

print("you can change values in a series")
print("you can do this by choosing the index of the value you want to change")
print("and then assigning it a new value\n")
mySeries["e"] = 100
print(mySeries)                                 # change a specific value
print("#"*10)
input()

print("you can select elements using boolean values")
print("True will return this element, and False will ignore it\n")
print(mySeries[[True,True,False,False,True]])                     # keep certain values
print("#"*10)
input()


print("you can select values if they meet a selection criteria")
print("in this case, i want to see if values are greater than zero or not\n")
print(mySeries > 0)                                    # see which values meet a certain criteria
print("#"*10)
input()

print("you can look at the series using this list (like in the example above") 
print("with the list of boolean values) to check this is working properly\n")
print(mySeries[mySeries > 0])
print("#"*10)
input()     # can compare list of boolean values (true/false) to the series to check if its working properly

print("you can use this line to change all of the negative values to positive values\n")
mySeries[mySeries < 0] *= -1
print(mySeries)
print("#"*10)
input() # change negative to positive values

print("pandas lets you do operations to every single item")
print("normally if you wanted to add 5 to every value in a list you would")
print("have to loop through the list and add 5 to every element")
print("")
print("in pandas you can do this:\n")
mySeries += 5
print(mySeries)
print("#"*10)
input()         # add a number to every single element in this series (in this case it's +5)

print("or divide every number by 2\n")
mySeries /= 2
print(mySeries)
print("#"*10)
input() # divide every single element in this series (in this is case it's /2) 

print("you can get the mean value in one line\n")
print(mySeries.mean())
print("#"*10)
input()         # find out mean value using the variabe name then ".mean"

print("if you try to add two series together and they don't have the")
print("same number of elements you will get NaN values\n")
mySeries += mySeries[mySeries > 5]
print(mySeries)
print("#"*10)
input()         # if one series has more/less elements then they won't add together


