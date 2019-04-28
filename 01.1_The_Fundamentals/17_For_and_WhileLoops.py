#For / While loops.
#For loops are used to iterate items in a list.

numbers = [0, 1, 2, 3, 4]
names = ["Michael", "Chris", "Ardan", "Nikita", "Jamie"]

for item in numbers:
       print(item)
#or
for item in names:
       print("This person's name is", item)

#While loops are used to conditionally iterate items in a list.

run = True
current = 1

while run:
       if current == 100:
             run = False
       else:
              print(current)
              current += 1
#This will print from 1-99.
#It will ONLY stop when the contition becomes False.
