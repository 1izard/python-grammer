# calender

import calendar
calendar.isleap(2000)   # True
calendar.isleap(2001)   # False



# datetime
# date & timedelta
# date : between 1-1-1 and 9999-12-31
from datetime import date
newyear = date(2020, 1, 1)  # datetime.date(2020, 1, 1)
newyear.year
newyear.month
newyear.day
newyear.isoform()   # 2020-01-01

from datetime import date, timedelta
now = date.today()
tomorrow = now + timedelta(days=1)
nextweek = now + timedelta(days=1) * 7


# time (from datetime)
from datetime import time
noon = time(12, 0, 0)
noon.hour
noon.minute
noon.second


# datetime
from datetime import datetime
some_day = datetime(2020, 1, 2, 3, 4, 5, 6)
some_day.isoformat()    # "2020-01-02T03:04:05.000006"

now = datetime.now()
now.year
now.month
now.day
now.hour
now.minute
now.second
now.microsecond


from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)

noon_today.date()
noon_today.time()



# time (Unix Time)
import time
now = time.time()   # 1391488263.664645
time.ctime(now)     # Mon Feb 3 22:31:03 2014

# to struc_time from Unix Time
time.localtime(now)     # standard time fo system (Not recommended because of including summer time)
time.gmtime(now)        # UTC (recommended)

# to Unix Time from struct_time
tm = time.localtime(now)
time.mktime(tm)

# strftime()
# form struct_time and return string
# %Y    1900-...
# %m    01-12
# %B    January,...
# %b    Jan, ...
# %d    01-31
# %A    Sunday, ...
# %a    Sun, ...
# %H    00-23
# %I    01-12
# %M    00-59
# %S    00-59
# %p    AM or PM
import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.strftime(fmt, time.gmtime(time.time()))
print(t)    # It's Saturday, December 15, 2018, local time 07:12:36PM

# strptime()
# from string to struct_time
fmt = "%Y-%m-%d"
time.strptime("2020-01-01", fmt)
time.strptime("2020 01 01", fmt)    # VauleError
time.strptime("2020-13-01", fmt)    # ValueError