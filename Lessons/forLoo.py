# For-Loops

cars = ['accord', 'celica', 240, 'hardbody', 'camaro', 'acadia', 'gsxr', 'G35', 'tundra', 'optima']

# for car in cars:
#     print(car) 

# for car in cars[1:3]:       # <-- "slicing" was used to gives us part of the list
    # print(car)


# as this function goes thru the collection( 'list' ) you can see that the condition statement written will cycle thru and output the values to what is met
for car in cars:
    if car == 'gsxr':
            print(f'{car} was my first motorcycle')
    else:
            print(f'{car} was one of the many vehicles I\'ve owned.')

# working a whileloop with a string of printing each index and letter
fruit = 'banana'
index = 0

while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# same code above but using a for loop
fruit = 'banana'
letter = None
for letter in fruit :
    print(letter)

# running a "count" using a for loop
word = 'papaya'
count = 0

for letter in word :
    if letter == 'a' :
        count = count + 1

print(count)