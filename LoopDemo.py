#A loop is a programming structure that can repeat a section of code 
#A loop can run the same code sxzctly over and over or with do,e thought it can generate a pattern

#There are two borad categories of loops
#Conditional Loops (While):	There loop as a long as a condition is true
#Counted loops(for): These loop using a counter to keep track of how many of thr loop has run.


#You can use any loop in any situation, but usually from deign perspective there is a better loop in terms of coding
#If you kno in advance how many times a loop should run a COUNTED LOOP is usually a better choice


#If you don't know how many timed a loop should tun a CONDITIONAL LOOP is usually a better choice




print("************************************************")
#Taking Inputs



word = ""


while (len(word) < 6 or word.isalpha() == False):
	#Loop block
	word = input("Please input a word larger than 5 letters: ")
	print(word.isalpha()) 
	if (len(word) < 6):
		print("Big Manz, I said less than five letters")

		if (word.isalpha() == False):
			print("Big Manz, I said a real word")



print(word+" is a seriously long word!")
#Do not use while loops to control inputs with GUI programs













