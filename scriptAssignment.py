
import os
import time
import datetime


f = os.listdir('/A/')
for x in f:
    item = os.path.join('C:\\A\\', x)
    if item.endswith('.txt'):
        time1 = os.path.getmtime(item)
        print("File:" + x + "Date modified: ", datetime.datetime.fromtimestamp(time1).strftime("%m/%d/%Y, %H:%M:%S"))




