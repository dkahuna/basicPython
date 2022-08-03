# def greet(name, time):
#     print(f'Good {time} {name}, hope you are well!' )

# know that the variables could be named anything and it would still work
# name = input("May I have your name: ")
# time = input("What time of the day is it where you're at: ")

# greet(name, time)


# to put a default value to the parameters of a function if function is called without any arguments (e.g. line 15) is with the '=' operator 
# def greet(name = 'ryu', time = 'morning'):
#     print(f'Good {time} {name}, hope you are well!')

# greet()

print("========Page 46 Python book==========")

def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

total_seconds = convert_days_to_seconds(7)
milliseconds = total_seconds * 1000
print(milliseconds)

