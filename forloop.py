
#for loop collecting user input and creating a list with string and integers
#encountered error trying to compile with python2, it generated nameError
# creating an empty list
lst = [ ]

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = (input("Enter your choice value. e.g int or string: "))

    lst.append(ele) # adding the element

print(lst)
