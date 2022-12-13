# A program to find the multiple of 3, 6 and 9 between (1 to 100) by list comprehension.


#Using Range fucntion to find the multiple of 3
mul_3 = [x for x in range(1,100) if x%3==0]
print("Multiplication of 3 between (1 to 100) is: \n", mul_3)

#Using Range fucntion to find the multiple of 6
mul_6 = [x for x in range(1,100) if x%6==0]
print("Multiplication of 6 between (1 to 100) is: \n",mul_6)

#Using Range fucntion to find the multiple of 9
mul_9 = [x for x in range(1,100) if x%9==0]
print("Multiplication of 9 between (1 to 100) is: \n",mul_9)

