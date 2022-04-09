print("-----Strings-----")

greeting = "Welcome!" #this is storing value
print(greeting) #returns the stored value above

name = input("What's your name? ") # this function prompts the user
print("Hi " + name + "!")
age = input("How old are you? ")
print("You are " + age + " " + "year(s) old") # storing the user's input will give feedback

# Lines 28 & 30 are examples of concatenating values, strings, etc.

print("-----Lists-----") #collections of data types

food = ["Wings", "What-A-Burger", "Donatos", "Surf&Turf", "SoCal Taco"] #storing more than one
print(food)
print(food[0]) # counting of a list starts at zero not 1
print(food[-1]) # start from right to left

spanishLine = "Buenos dias, amigo."
print(spanishLine.split(' ')) #this will break the string into a list due to space argument passed in
