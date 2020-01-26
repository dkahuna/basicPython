
# FORMAT METHOD
chineseRat = 'Rat'
chineseOx = 'Ox'

print('This year 2020 is the year of the {0}, and next year will be the year of {1}'.format(chineseRat, chineseOx)) # <-- placing these here puts them in an index lineup

num1 = 8.2589116
num2 = 95.7895698

# this format uses the semicolon and places wanted to show, also notice the ' f ' changing the output as well
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))

#using F-STRINGS
print(f'num 1 is {num1:.4f} and num 2 is {num2:.3f}')   #notice th  " f " used in the beiginning of the opening string and also to output after the decimal place
