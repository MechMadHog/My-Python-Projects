#Importing Libraries into a Script.
#Modules are EXTERNAL libraries that can be included in a given project.
#Modules provide extra pre-built functionality to a project.

import re
#"re" is  RegEx aka the Regular Expressions library.
#RegEx is included with Python so nothing will have to be installed on my system.

string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
print(string)

#new = re.sub('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', ' ', string)
#Rather than listing every character RegEx allows for a range to be selected.
#new = re.sub('[A-Z]', '', string)
#new = re.sub('[a-z]', '', string)
new = re.sub('[.,\'+" "]', '', string)
#.sub i.e. the Substitute function can replace characters.
#Rules within RegEx are contained within "[]".
#+" " allows for spacing to also be removed.
#^ will remove all except for what follows "^".
print(new)

