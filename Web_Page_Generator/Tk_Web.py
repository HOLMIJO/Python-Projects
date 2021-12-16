import webbrowser
import os
from tkinter import *

# Defines Submit function and defines parameters
# for the HTML to place user determined text
# and to write said text as the body of HTML file.


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
    webbrowser.open_new_tab("WebGen.html")


window = Tk()  # this is the GUI
btn = Button(window, text="To confirm body click here",
             fg='black', command=Submit)
btn.place(x=80, y=100)
txtfld = Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Web Page Generator')
window.geometry("300x200+10+10")
window.mainloop()
