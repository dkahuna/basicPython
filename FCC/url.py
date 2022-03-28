import urllib.request, urllib.parse, urllib.error

# library that makes the socket call to 'GET' the url data
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    # decrypts the lines from URL to UTF-8 array and then strips it into a string
    print(line.decode().strip())