#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use
import tkinter as tk 






root = tk.Tk()









labUN = tk.Label(root, text = "User Name")


labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx = 10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root, show = "*")
entPassword.pack()

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()





root.mainloop()


