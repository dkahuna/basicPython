fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

for line in hand :
    line = line.rstrip()
    print(line)
