# overview 
'''Use numeric data types
Use string data types
Use the list data type
Use a for loop
Use the print() function'''

# Exercise 1: Creating a mixed-type list
myMixTypeList = [45, 2345523, 1.02, True, "I like Sugar.", "45"]
for item in myMixTypeList:
    print("{} is the data type {}".format(item, type(item)))