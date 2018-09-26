#This file will go through the basics of manipulation
#String manipulation

#Strings are collections of characters 
#Strings are enclosed in "" or ''
# "Paul is cool"
# "Paul is cool!"
#Two things we need to talk about when we think of strings\
#index - Always starts at 0
#length

#Example
# 0123    012345

name = "Ben"

print(name) # I can print strings

sentence = name + "Is the best"
print(sentence)

print(sentence + "!")

#I can also do specific letters
fletter = name [0]
print (fletter)

letters1 = name [0:2] #inclusive:exclusive
print(letters1)

letters2 = name [2:]
print(letters2)

letters2a = name [2:len(name)]

letters3 = name[:2]
print(letters3)

#If I want to print out all letters
for i in range(len(name)):
	print(name[i])
	