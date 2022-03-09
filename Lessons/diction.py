# another data type of Python: 'Dictionaries'
ninja_belts = {"Crystal": "Blue", "Ryu": "Black"}

# Dictionaries are object oriented like in JavaScript; being key value pairs
# being 'dict' , short for Dictionary
print(ninja_belts)

# outputs dict_keys(["Crystal", "Ryu"]) <---- keys only, no values that are assigned if any
print(ninja_belts.keys())

# to put it into a better perspective to read is using a list() method. Better yet an array
print(list(ninja_belts.keys()))
print(ninja_belts.values())

# searching within a dictionary to see what keys/values lie within using the count method but first turn into a list() of a variable
key = list(ninja_belts.keys())
print(key.count("Ryu"))

vals = list(ninja_belts.values())
print(vals.count("Blue"))

# to update a dictionary, write out the dictionary to update along with the following below - dictionary[key string] = value string
ninja_belts["Yoshi"] = "Green"
# the above will be push to the end of the dictionary
print(ninja_belts)

# another way to define a dictionary or you may see
person = dict(name = "David", age = 33, height = "6ft 4in")
print(person)

print("=========Below is a progam example==================")

# creating a function to loop thru the dictionary of ninjas that the user inputs starting on line 37
def ninja_Roll_Call(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am a {val} belt!")

# main dictionary to work with this progam example
ninja_Rank = {}

while True:
    ninja_Name = input("Enter a name for the ninja: ")
    ninja_Belt = input("What is the ninja's belt color rank: ")
    # to update the dictionary, you must assign the key/value pair to the desired dictionary made line 39
    ninja_Rank[ninja_Name] = [ninja_Belt]

    another_Ninja = input("Is there another ninja to add? (y/n)")
    if another_Ninja == "y":
        continue
    else:
        break

# calling the function - line 34
ninja_Roll_Call(ninja_Rank)