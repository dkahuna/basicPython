# if-statements which are for meeting certain conditions and outputting their values

age = int(input('Enter your age: '))

if age < 21:
    # code block / notice that 'indenting' is very IMPORTANT in Python
    print('You are not of legal age to purchase alcohol.')
elif age >= 21:
    print('You are able to purchase alcohol at this establishment.')

drip = input('Do you love coffee? (y/n): ')

if drip != "y":     # notice that '!=' is for *not equal*
    # again this is a code block
    print('I will make some hot tea for you then!')
else:
    print('Do you prefer it with cream&sugar or black?')