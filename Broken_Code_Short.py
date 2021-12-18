from tkinter import filedialog
from tkinter import *
import os
import time
import shutil
root = Tk()
root.title('Welcome to File Manager')
root.geometry("500x350")

# Allows user to select source folder


def chooseSource():
    src = filedialog.askdirectory()
    # C:\Users\joeho\Desktop\Playground\folderA
    srcEntry.insert(0, src)
# Allows user to select destination folder


def chooseDest():
    dest = filedialog.askdirectory()
    # C:\Users\joeho\Desktop\Playground\folderB
    destEntry.insert(0, dest)

# Checks time modified on files for last 24 hours
# before preparing to transfer files.


def transferFiles():
    # grabs the source path from srcEntry widget
    sourcePath = srcEntry.get()
    # grabs the destination path from destEntry widget
    destPath = destEntry.get()
    # Sets parameters for the 24 hour window
    SECONDS_IN_DAY = 24 * 60 * 60
    now = time.time()
    before = now - SECONDS_IN_DAY


# Determines if modified within 24 hours

    def last_mod_time(fname):
        return os.path.getmtime(fname)
# Checks to see if file has been modified in 24 hours
# If files match then move to destination folder
    for fname in os.listdir(sourcePath):
        src_fname = os.path.join(sourcePath, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(destPath, fname)
            shutil.move(src_fname, dst_fname)
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ", folderList, "folder are:")
    while(i < len(sortlist)):
        print(sortlist[i]+'\n')
        i += 1


srcEntry = Entry(root)
srcEntry.pack(pady=26)
destEntry = Entry(root)
destEntry.pack(pady=28)

# Button widget for choosing the source folder
srcButton = Button(root, text="Choose Source Folder", command=chooseSource)
srcButton.pack(pady=24)
# Button widget for choosing the destination folder
destButton = Button(root, text="Choose Destination Folder", command=chooseDest)
destButton.pack(pady=26)
# Tkinter button to check files in selected source folder
check_button = Button(root, text="File Check", command=transferFiles)
check_button.pack(pady=24)
# root mainloop to keep Tkinter alive
root.mainloop()
