import tkinter as tk

#1. Want to take an inteer input
#2. If it is an integer I want to store the value
#3. If it is a string I don't want it to crash
def submit(*args):

	#Try the code, if things go wrong it stops
	#and jumps to the except code and runs it. 
	try: 
		print("Submit Pressed")
	
		x1 = int(ent1.get()) #cast to int CRASHER!!!
		ent1.delete(0,tk.END)
		
		x2 = int(ent2.get()) #cast to int CRASHER!!!
		ent2.delete(0,tk.END)
	
		answers.append(x1) #append to list called answers
		answers.append(x2) #append to list called answers
		

	except:
		print("DUDE, I SAID AN INTEGER")

	print(answers)
answers = []
root = tk.Tk()

ent1 = tk.Entry(root)
ent1.pack()
ent2 = tk.Entry(root)
ent2.pack()
btn1 = tk.Button(root, text = "Submit", command = submit)
btn1.pack()


root.mainloop()