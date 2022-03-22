fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict() #making an empty dictionary
for line in hand :
    line = line.rstrip() #this line strips the white space on the right side per line of the file
    # print(line)
    words = line.split() #this line splits the text file into an array
    # print(words)
    for wds in words:
        print(wds)
        if wds in di :
            di[wds] = di[wds] +1
            print('**Existing**')
        else:
            di[wds] = 1
            print('**NEW**')
        print(di[wds])

print(di)

