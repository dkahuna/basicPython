# using modules: keyword 'import'
import webbrowser

# using the module name before the built in function name to use
webbrowser.open('http://docs.python.org/3/library')

# importing only the function wanted from the module 'import'-ed
from random import choice

# randomly chooses from the list made
direction = choice(['N', 'S', 'E', 'W'])

print(direction)

# renaming a built-in function to fit your needs from what is 'import'-ed
from time import time as time_now

# built-in function 'time' is known now as 'time_now'
now = time_now()

print(now)