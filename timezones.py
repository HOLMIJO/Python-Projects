
import datetime as dt
from datetime import datetime
import pytz

dt_today = datetime.now()  # Local time
dt_Portland = dt_today.astimezone(pytz.timezone('America/Los_Angeles'))
dt_NewYork = dt_today.astimezone(pytz.timezone('America/New_York'))
dt_London = dt_today.astimezone(pytz.timezone('Europe/London'))
Portland = (dt_Portland.strftime('%m/%d/%Y %H:%M'))
NewYork = (dt_NewYork.strftime('%m/%d/%Y %H:%M'))
London = (dt_London.strftime('%m/%d/%Y %H:%M'))

if dt_today.hour > 9 and dt_today.hour <= 17:
    print("Yes, we're open!")
else:
    print("We're closed!")


print("Pacific Standard Time: "+Portland+" PST")
print("Eastern Standard Time: "+NewYork+" EST")
print("British Summer Time: "+London+" BST")
