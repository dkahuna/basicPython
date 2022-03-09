# RANGES

    # a method to cycle/run thru a list/array of numbers that is passed through in the argument(s) but note that it not inclusive


# this will print everthing from 0 to 7, not 8
for spot in range(8):
    print(spot)

print("--- Lines 13&14 ---")

# passing more than one in the argument will give it a starting point but same thing occurs with not printing the end point
for place in range(5, 13):
    print(place)

print("----- Lines 18&19 ------")
# a third argument can be passed thru for stepping thru in pattern
for increments in range(0,100,10):
    print(increments)

print("--- Lines 23 thru 26 ---")
# printing with index
burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

for burger in range(len(burgers)):
    print(burger, burgers[burger])

print("--starting point at end of list--")
# this next block will print counting backwards but also including what should be exclusive
for burger in range(len(burgers)-1, -1, -1):
    print(burger, burgers[burger])
