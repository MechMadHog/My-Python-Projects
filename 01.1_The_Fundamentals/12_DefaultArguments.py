#A Default Argument is an argument that appears when no value has been given.

def print_something(name = "Michael", age = "Unknown"):
    print("My name is",  name,  "and my age is", age)
    #When printing a number of different things; concatenation is no longer necessary.
    #When using concatenation it is NECESSARY to  make age a String.
    #i.e. str(age).

#print_something("Michael", 29)
#When the value has been given.
print_something("Michael")
