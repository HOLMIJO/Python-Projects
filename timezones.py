import datetime as dt
from datetime import datetime
import time
import pytz

dt_today = datetime.datetime.today() # Local time
dt_Portland = dt_today.astimezone(pytz.timezone('America/Los_Angeles'))
dt_NewYork = dt_today.astimezone(pytz.timezone('America/New_York'))
dt_London = dt_today.astimezone(pytz.timezone('Europe/London'))
Portland = (dt_Portland.strftime('%m/%d/%Y %H:%M'))
NewYork = (dt_NewYork.strftime('%m/%d/%Y %H:%M'))
London = (dt_London.strftime('%m/%d/%Y %H:%M'))

nw = datetime.now()
hrs = nw.hour;mins = nw.minute;secs = nw.second;
zero = timedelta(seconds = secs+mins*60+hrs*3600)
st = nw - zero #This takes me to 0 hours.
time1 = st + timedelta(9*3600+00*60) #This gives 9:00AM
time2 = st + timedelta(seconds=17*3600+00*60) #This gives 5:00PM
if nw>= time1 or nw <= time2:
    print("Yes, we're open!")
else:
    print("We're closed!")

"""def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:
        #Over midnight
        return nowTime >= startTime or nowTime <= endTime
isNowInTimePeriod(dt.time(9,00), dt.time(17,00), dt.datetime.now().time())
"""
        
print("Pacific Standard Time: "+Portland+" PST")
print("Eastern Standard Time: "+NewYork+" EST")
print("British Summer Time: "+London+" BST")
