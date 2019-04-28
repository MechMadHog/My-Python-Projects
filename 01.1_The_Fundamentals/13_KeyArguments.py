#A Key Argument is an argument that targets SPECIFIC arguments.


def print_something(name="Unknown Name", age="Unknown"):
    print("My name is",  name,  "and my age is", age)


# "None" is the equivalent of "Null" in other programming languages.
# The term "None" is  a boolean value.
#print_something(None, 27)
print_something(age=29)
# When using Key Arguments, order does not matter.
print_something(age=29, name="Michael")
