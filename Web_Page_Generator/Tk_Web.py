import webbrowser
import os
from tkinter import *


def Submit():
    text = txtfld.get()
    html_template = """
    <html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>
    """.format(text)
    f = open("WebGen.html", "w")
    # writing code into file
    f.write(html_template)
    f.close()


filename = 'C://Users//joeho//Dropbox//School//Python-Projects//Web_Page_Generator' + \
    os.getcwd()+'//' + 'WebGen.html'
webbrowser.open_new_tab(filename)

window = Tk()  # this is the GUI
btn = Button(window, text="To confirm body click here",
             fg='black', command=Submit)
btn.place(x=80, y=100)
txtfld = Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Web Generator')
window.geometry("300x200+10+10")
window.mainloop()
