# For-Loops

cars = ['accord', 'celica', 240, 'hardbody', 'camaro', 'acadia', 'gsxr', 'G35', 'tundra', 'optima']

# for car in cars:
#     print(car) 

# for car in cars[1:3]:       # <-- "slicing" was used to gives us part of the list
    # print(car)

for car in cars:
    if car == 'gsxr':
            print(f'{car} was my first motorcycle')
    else:
            print(f'{car} was one of the many vehicles I\'ve owned.')