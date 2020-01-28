# while loop

age = 25

num = 0

while num < age:
    # block of code       *alert* switching the lines of code 9&10 will output different results; one will spit out the num zero first and the other the number one
    if num % 2 == 0:            #practicing a conditional statement within the loop
        print(num)
    if num > 10:
        break          #this here is to stop the 'while loop' from running after a condition is met
    num += 1