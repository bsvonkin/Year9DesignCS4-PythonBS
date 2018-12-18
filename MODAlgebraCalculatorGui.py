import tkinter as tk
from PIL import ImageTk, Image
import math


root = tk.Tk()
root.title("Algebra Calculator")

def calculation():
	global temp
	entAnswer.config(state="normal")
	entAnswer.delete(0, tk.END)
	entAnswer.insert(0,str(eval(temp)))
	entAnswer.config(state="disable")
	entSteps.config(state="normal")
	entSteps.delete(0, tk.END)
	entSteps.insert(0,str(temp))

	entSteps.config(state="disable")

	
	


def selected(event):
	print("selected")
	

	print(event.widget["text"])
	opt = event.widget["text"]

	if opt == "Square":
		global temp
		entUN.insert(0,"")
		entUN.insert(tk.END,"^2")
		temp = entUN.get()
		
		temp = temp.replace("^","**")
		print(temp)
		print(eval(temp))

	print(event.widget["text"])
	opt = event.widget["text"]

	if opt == "Square Root":
		temp = entUN.get()
		entUN.delete(0,tk.END)
		entUN.insert(0,"√("+temp+")")
		#entUN.insert(tk."x**(1/2)")
		temp2 = entUN.get()
		temp2 = temp2[2:len(temp2) - 1] + "**(1/2)"
		
		#print("****"+ctemp2)
		print(eval(temp2))
		
		#print(event.widget["text"])
	opt = event.widget["text"]

	




labUN = tk.Label(root, text = "Equation")
labUN.grid(row=1, column=0, columnspan = 2)



entUN = tk.Entry(root, bg="#F0F0F0")
entUN.grid(row=2, column=0, columnspan = 2)


labellist = [] 

labellist.append(tk.Label(root, text = "Square")) 
labellist.append(tk.Label(root, text = "Square Root")) 

labellist[0].grid(row = 3, column = 0)
labellist[1].grid(row = 3, column = 1)

labellist[0].bind("<Button-1>",selected)
labellist[1].bind("<Button-1>",selected)

btnSubmit = tk.Button(root, text = "Submit", command=calculation)
btnSubmit.grid(row=6, column=0, columnspan = 2)



def change(*args):
	print("running change")
	print(var.get())


OPTIONS = [
	"All Steps",
	"No Steps",
	"Step by Step",
]

var = tk.StringVar()
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.grid(row=8,column=2)




labPassword = tk.Label(root, text = "Answer")
labPassword.grid(row=9, column=0)



entAnswer = tk.Entry(root, bg="#F0F0F0")
entAnswer.grid(row=10,column=0,)
entAnswer.config(state = "disable")

labSteps = tk.Label(root, text = "Steps")
labSteps.grid(row=11, column=0)

entSteps = tk.Entry(root, bg="#F0F0F0")
entSteps.grid(row=12, column=0)
entSteps.config(state = "disable")



img = ImageTk.PhotoImage(Image.open("x-squared-pic.png"))

panel1 = tk.Label(root, image=img)

panel1.grid(row=4, column=0)

img1 = ImageTk.PhotoImage(Image.open("square-root-pic.png"))

panel2 = tk.Label(root, image=img1)

panel2.grid(row=4, column=1)


root.mainloop()










