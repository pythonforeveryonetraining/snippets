from tkinter import Tk
from tkinter import Label
from tkinter import Listbox
from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import StringVar

employees = [("Vera", "Schmidt"), ("Chuck", "Murphy"), ("Dave", "Dreissig")]

def add_employee():
    employees.append((firstname_binder.get(), lastname_binder.get()))  
    employees_binder.set(employees)
    
def delete_employee():
    index = listbox_employees.curselection()[0]  
    employees.pop(index)
    employees_binder.set(employees)
    
window = Tk()
window.geometry("520x300")
window.title("Employees")

label_employees = Label(window, text="Employees")
# label_employees.pack()
label_employees.grid(column=0, row=0, padx=(20, 20), sticky="w")  # w(est)

employees_binder = StringVar(value=employees)
listbox_employees = Listbox(window, height=14, listvariable=employees_binder)  
listbox_employees.grid(column=0, row=1, padx=(20, 20))

button_delete_employee = Button(window, text="Delete", command=delete_employee)
button_delete_employee.grid(column=0, row=2, padx=(20, 20), sticky="w")

frame_input = Frame(window)
frame_input.grid(column=1, row=1, sticky="n")

label_firstname = Label(frame_input, text="First name")
label_firstname.grid(column=0, row=0)

firstname_binder = StringVar()
entry_firstname = Entry(frame_input, textvariable=firstname_binder)
entry_firstname.grid(column=1, row=0)

label_lastname = Label(frame_input, text="Last name")
label_lastname.grid(column=0, row=1)

lastname_binder = StringVar()
entry_lastname = Entry(frame_input, textvariable=lastname_binder)
entry_lastname.grid(column=1, row=1)

button_add_employee = Button(frame_input, text="Add", command=add_employee)
button_add_employee.grid(column=1, row=2, sticky="w")

window.mainloop()
