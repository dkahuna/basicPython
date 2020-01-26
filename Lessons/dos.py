# -- Continued from Pg. Uno (Format Method)

num1 = 8.2589116
num2 = 95.7895698

# this format uses the semicolon and places wanted to show, also notice the ' f ' changing the output as well
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))

#using F-STRINGS
print(f'num 1 is {num1:.4f} and num 2 is {num2:.3f}')   #notice th  " f " used in the beiginning of the opening string and also to output after the decimal place

