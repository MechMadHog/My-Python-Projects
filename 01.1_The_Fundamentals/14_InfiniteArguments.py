#An Infinite Argument is used to declare a FLEXIBLE number of arguments.


def print_people(*people):
       for person in people:
          print("This person is", person)

print_people("Michael", "Chris", "Ardan", "Nikita", "Jamie")
