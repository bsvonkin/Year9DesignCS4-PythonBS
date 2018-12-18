import tkinter as tk 






root = tk.Tk()
root.title("Algebra Calculator")



def dab():
	print("dab")



labUN = tk.Label(root, text = "Equation")
labUN.grid(row=1, column=0)

entUN = tk.Entry(root, bg="#F0F0F0")
entUN.grid(row=2, column=0)


btnSubmit = tk.Button(root, text = "Submit", command = dab)
btnSubmit.grid(row=3, column=0)



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
dropDownMenu.grid(row=5,column=1)




labPassword = tk.Label(root, text = "Answer")
labPassword.grid(row=5, column=0)



entAnswer = tk.Entry(root, bg="#F0F0F0")
entAnswer.grid(row=6,column=0,)
entAnswer.config(state = "disable")

labSteps = tk.Label(root, text = "Steps")
labSteps.grid(row=7, column=0)

entSteps = tk.Entry(root, bg="#F0F0F0")
entSteps.grid(row=8, column=0)
entSteps.config(state = "disable")



root.mainloop()










