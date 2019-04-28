#if, elif, else are conditional statements.
#elif statements MUST come between if and else statements.

#check =  False
#check = True
check = "Neither"
#check = "Either"

if check == False:
       print("It is False!")
elif check == "Neither":
       print("It isn't actually True of False?")
elif check == "Either":
       print("It is actually Both!")
else:
       print("It is actually equal to True!")
