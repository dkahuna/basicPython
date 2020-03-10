my_name = "Kahuna"  # this is global 

def print_name():
    global my_name #overrides the local
    my_name = "David"
    print('the name inside this function is', my_name)


print_name()
print('outside the function the name is', my_name)