'''
datetime module usage

'''
from datetime import datetime, timezone
from time import mktime

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print('now =', now)
print('now_utc =', now_utc)
print('now_local =', now_local)
# now = 2014-08-10 18:18:30
# now_utc = 2014-08-10 18:18:30+00:00
# now_local = 2014-08-11 03:18:30+09:00

time_format = '%Y-%m-%d %H:%M:%S'
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print('now =', now)
print('type(now) =', type(now))
print('time_tuple =', time_tuple)
print('utc_now =', utc_now)
# now = 2014-08-10 11:18:30
# type(now) = <class 'datetime.datetime'>
# time_tuple = time.struct_time(tm_year=2014, tm_mon=8, tm_mday=10, tm_hour=11, tm_min=18, tm_sec=30, tm_wday=6, tm_yday=222, tm_isdst=-1)
# utc_now = 1407637110.0
'''
It's OK to use time.mktime() because not used local time here.
'''

arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_nav
