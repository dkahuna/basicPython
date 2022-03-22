fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict() #making an empty dictionary
for line in hand :
    line = line.rstrip() #this line strips the white space on the right side per line of the file
    words = line.split() #this line splits the text file into an array
    # print(words)
    for wds in words:
            # idiom: retrieve/create/update counter
            di[wds] = di.get(wds,0) + 1

# print(di)

#now to find the most common word
largest = -1
theWord = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theWord = k #capture and remember the largest 'key'

print('The most common word used is:', theWord, largest)