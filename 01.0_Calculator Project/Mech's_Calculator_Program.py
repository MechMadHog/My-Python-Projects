# Mech's Calculator Program is a calculator that can perform basic math equations.
#Until the program is closed.
import re

print("Welcome to Mech's Calculator Program!")
print("Please type 'exit' to close Mech's Calculator Program!\n")
# \n will add a new line

previous = 0
run = True


def perform_math():
    global run
    global previous
    # The global function adds the run variable to my math function.
    equation = ""
    if previous == 0:
        equation = input("Please enter your equation: ")
    else:
        equation = input(str(previous))
    if equation == 'exit':
        print("You have exited Mech's Calculator Program!, Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        # It is  not recommended to  use the eval function outside of the parameters of a calculator.
        # Using RegEx prevents a user from doing something unconventional that could crash the program.
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        #print("The equation you have entered is", previous)


while run:
    perform_math()
