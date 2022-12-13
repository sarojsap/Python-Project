#Analysing data using pandas

#Impoting module
import pandas as pd

#Importing .csv file into python
dt = pd.read_csv('earthquake.csv')

#Using DataFrame data structure.
dt1 = pd.DataFrame(dt)
print(dt1)

#Now we are going to analyse our data.
#Using head() method
print("These are the first five rows of this data.")
print(dt1.head()) #it will give the first five rows

#Using tail()method
print("These are the last eight rows of this data.")
print(dt1.tail(-8)) #it will give the last 8 rows


print("This is the overall info about this data.")
print(dt1.info())

#Printing data in descending order according to Magnitude
print("Data in descending order according to Magnitude")
print(dt1.sort_values(by = 'Magnitude', ascending= False))

print("Earthquakes with equal and more than 5.0 Magnitude.")
print(dt1[dt1['Magnitude']>=6.5]) #Earthquakes with more than 6.5 Magnitude

print("Names of all epicentre: \n ")
print(set(dt1['Epicentre'])) # Prints the name of all epicentres.



#Now we will plot our data, for which we require another module
#Importing Module

import matplotlib.pyplot as plt

dt.plot()
#Labelling x-axis
plt.xlabel("Number of earthquakes")

#Labelling y-axis
plt.ylabel("Richter Scale")
plt.show()



