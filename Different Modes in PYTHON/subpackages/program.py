# what can you import
# a particular function inside python file (module)
# a python file (package)

# there are two ways to use package in Python
# (1) from <package_directory> import <package_name>
# (2) import <package_directory>.<package_name>


## MODULE #######################
# to import just module(function)
# from demo.myfunction import cube 
# cube(50)

# to import just module(function) as another_name
# from demo.myfunction import cube as c
# c(50)


## PACKAGE #######################
# from demo import myfunction
# myfunction.cube(5)

# import demo.myfunction
# demo.myfunction.cube(8)

# import demo.myfunction as dm
# dm.cube(8)
# print(dm.colors);
# print(dm.names);
# print(type(dm.colors));
# print(type(dm.names));

## SUBPACKAGE #####################
# from demo.bio import display
# import demo.bio.display
# display.show()


# from demo.science.chemistry.physics import display
# display.show()

# import demo.science.chemistry.physics.display
# demo.science.chemistry.physics.display.show()

# import demo.science.chemistry.physics.display as ds
# ds.show()


