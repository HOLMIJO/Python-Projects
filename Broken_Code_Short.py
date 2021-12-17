from tkinter import filedialog
from tkinter import *
import os
import time
import shutil
root = Tk()
root.title('Welcome to File Manager')
root.geometry("500x350")

# User chooses source directory


def select_folder():
    # ** src is disconnected. Not sure how to attach **
    src = filedialog.askdirectory()

# User chooses destination directory


def move_to():
    src = filedialog.askdirectory()
    dst = filedialog.askdirectory()
# Sets parameters for the 24 hour window
    SECONDS_IN_DAY = 24 * 60 * 60
    now = time.time()
    before = now - SECONDS_IN_DAY
# Determines if modified within 24 hours

    def last_mod_time(fname):
        return os.path.getmtime(fname)
# Checks to see if file has been modified in 24 hours
# If files match then move to destination folder
    for fname in os.listdir(src):
        src_fname = os.path.join(src, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(dst, fname)
            shutil.move(src_fname, dst_fname)

# Folder list sorts files meeting criteria
# then prints list


def file_check():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ", folderList, "folder are:")
    while(i < len(sortlist)):
        print(sortlist[i]+'\n')
        i += 1


# Tkinter button for source folder selection
select_button = Button(root, text="Select Source Folder",
                       command=select_folder)
select_button.pack(pady=20)
# Tkinter button for destination folder selection
move_button = Button(root, text="Move To Destination Folder", command=move_to)
move_button.pack(pady=22)
# Tkinter button to check files in selected source folder
check_button = Button(root, text="File Check", command=file_check)
check_button.pack(pady=24)
# root mainloop to keep Tkinter alive
root.mainloop()
