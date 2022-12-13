# Display and plot even numbers between 2 and 200.

#imporing modules
import matplotlib.pyplot as plt

newlist = [x for x in range(2,200) if x%2==0]
print("Even numbers betweem (2 to 200) are: \n", newlist)

plt.plot(newlist)

#Labelling x-axis
plt.xlabel("Even Numbers")

#Labelling y-axis
plt.ylabel("Range")

plt.show()









