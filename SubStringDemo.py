#Input
fName = input("What is your first name: ")
lName = input("What is your last name: ")

#Process
result = fName[0] + "." + lName
codeName = fName[0] + fName[1] +fName[2] + "." + lName[2] + lName[4]

#Output
print("Nice to see you" + result)
print("Your code name is" + codeName)