from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os

#basic stuff
root = Tk()
root.title('PDF Merger - GUI')
size_x = 300
size_y = 300
root.geometry(f'{size_x}x{size_y}')

#directory selecter function
def select_dir(entry):
    path = askdirectory()
    entry.delete(0, END)
    entry.insert(0, path)

#target selection stuff
btn_target = Button(root, text='Select target directory', command= lambda: select_dir(txt_target))
txt_target = Entry(root)

txt_target.grid(row= 0)
btn_target.grid(row= 1)

#add space between
spacer = Label()
spacer.grid(row= 2)

#output stuff
btn_output = Button(root, text='Select output directory', command= lambda: select_dir(txt_output))
txt_output = Entry(root)

txt_output.grid(row= 3)
btn_output.grid(row= 4)

#add space between
spacer.grid(row= 5)

#execute button
def execute():

    args = ''

    #check if selected folders are valid
    if txt_target.get() != '' and os.path.isdir(txt_target.get()):
        args += f'-t "{txt_target.get()}" '
    if txt_output.get() != '' and os.path.isdir(txt_output.get()):
        args += f'-o "{txt_output.get()}" '
    
    os.system(f'pdf_merger.py {args}')
    tkinter.messagebox.showinfo(title= None, message= 'Files merged')

btn_execute = Button(root, text= 'Execute', command= execute)
btn_execute.grid(row= 6)

root.mainloop()