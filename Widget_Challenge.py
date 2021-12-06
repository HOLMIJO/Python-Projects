import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from typing import Optional
tkinter.filedialog.askdirectory()

class One( Frame ):
    def __init__( self, master ):
        tk.Frame.__init__(self)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 200))
        
        self.master.title("Check Files")
        self.master.config(bg='lightgray')

        self.varFName1 = StringVar()
        self.varFName2 = StringVar()

        self.txtFName1 = Entry(self.master, text=self.varFName1, font=("Helvetica", 16), fg='lightgray', bg='white')
        self.txtFName1.grid(row=3, column=2, columnspan = 2, padx=(30,0), pady=(30,0))

        self.txtFName2 = Entry(self.master, text=self.varFName2, font=("Helvetica", 16), fg='lightgray', bg='white')
        self.txtFName2.grid(row=4, column=2, columnspan = 2, padx=(30,0), pady=(10,0))
        
        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1, command=self.submit)
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(30,0), sticky=NW)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1, command=self.submit)
        self.btnBrowse2.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=NW)

        self.btnCkFiles = Button(self.master, text="Check for files...", width=20, height=2, command=self.submit)
        self.btnCkFiles.grid(row=5, column=0, padx=(30,0), pady=(30,0), sticky=NW)

        self.btnClose = Button(self.master, text="Close Program", width=20, height=2, command=self.close)
        self.btnClose.grid(row=5, column=3, padx=(30,0), pady=(10,0), sticky=SE)


    def browse_button():
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        print(filename)
            
    
    def callback():
        name= fd.askopenfilename()
        print(name)

    errmsg = 'Error!'
    tk.Button(text='Click to Open File',
                command=callback).pack(fill=tk.X)
    tk.mainloop()

        
    def close(self):
        self.root.destroy()
        
        
    def submit(self):
        fn1 = self.varFName1.get()
        fn2 = self.varFName2.get()
        self.lblDisplay.config(text='Searching for {} and {}!'.format(fn1,fn2))
        

if __name__ == '__main__':
    root = Tk()
    App = One(root)
    root.mainloop()
