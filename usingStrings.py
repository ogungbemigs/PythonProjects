#using String methods


firstName = input ("Enter your First name: " )
lastName = input ("Enter your Last Name: ")
email = input ("Enter your email: ")
y =email.split('@')

fullName = firstName + " " + lastName

print("Your full Name is {} ".format(fullName))

#using the string uppercase function
print("..........Using Upper Case function.......................")
print (fullName.upper())

print("--------Using the Split Function-------------------")
#using Strings split function
print(fullName.split())


print("...........More on Split, specifying where to split words.......")
print(email.split('@'))

print(type(y))



