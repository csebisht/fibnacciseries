import tkinter as tk
from tkinter import ttk
from tkintermodule import action
win =tk.Tk()
win.title('Pradeep')

Username_label=ttk.Label(win,text='Username')
Username_label.grid(row=0,column=0,sticky=tk.W)
Username_label_var=tk.StringVar
Username_label=ttk.Entry(win,width=16,textvariable=Username_label_var)
Username_label.grid(row=0,column=1)

name_label=ttk.Label(win,text='Name')
name_label.grid(row=1,column=0,sticky=tk.W)
name_var=tk.StringVar
name_text=ttk.Entry(win,width=16,textvariable=name_var)
name_text.grid(row=1,column=1)

Email_label=ttk.Label(win,text='Email')
Email_label.grid(row=2,column=0,sticky=tk.W)
Email_var=tk.StringVar
Email_label=ttk.Entry(win,width=16,textvariable=Email_var)
Email_label.grid(row=2,column=1)

Mobile_label=ttk.Label(win,text='Mobile')
Mobile_label.grid(row=3,column=0,sticky=tk.W)
Mobile_var=tk.StringVar
Mobile_label=ttk.Entry(win,width=16,textvariable=Mobile_var)
Mobile_label.grid(row=3,column=1)

save_button=ttk.Button(win,text='Submit',command=action)
save_button.grid(row=4,column=0,sticky=tk.W)
win.mainloop()

