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

print("-----Strings-----")

name = "Kahuna" #this is storing value
print(name) #returns 'Kahuna'

age = input("How old are you? ") # this function prompts the user
print("You are " + age + "year(s) old") # storing the user's input will give feedback