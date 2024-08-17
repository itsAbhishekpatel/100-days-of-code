# Pypi = Python package index 
# form there you can search and install packages which you can use in you project
# Look into the documentation and know how to use it 
# Add an external library to your project and use it 

import prettytable as pt

# create an object table belongs to prettytable class   
table = pt.PrettyTable()
table.field_names = ["Pokemon Name","Type"]
table.add_rows(
    [
        ["Pikachu","Electic"],
        ["Charamender","Fire"],
        ["Squirtle","Water"]
    ]

)
print(table) # center align
# you can chnage the attribute as well - data is center align for now
table.align = "l"
print(table)

# objects are great they will do all things for you - 
"""-make the object and call the associate method to do that task and
 you do not worry about the implementation of this function at all. """
