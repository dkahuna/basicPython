# everything in Python is considered 'OBJECTS' and note that objects have "attributes" & "methods"

# and "methods" are respectedly functions towards the 'object' at hand

# understanding of numbers, strings, and lists

# print() <--- is key!!!! Unless within cmd

print("----------------------------")
print(type(5))      # returns the <class 'int'> for integer
print("----------------------------")
print(type(10.5))  # returns the <class 'float'> for non-whole numbers
print("----------------------------")
print(5 + 5)  #returns 10
print(5 - 5) #returns 0
print(5 * 5) #returns 25
print(5 / 5) #returns 1.0 <-- which is a float
print(5 // 5) #returns 1 <-- which is an integer
print(5 ** 5) #returns the power of; 3125
print(25 % 2) #returns the remainder 1

num = 88    #storing an integer
num += 2   #this changes the value due to having the equal sign after the operation
print(num)  #returns 90





# Calculating the area of a circle
radius = input('Enter the radius of your circle (m): ')
area = 3.142 * int(radius)**2  # int() function is used to convert the user's input from string to integer
print('The area of your circle is:', area) 

