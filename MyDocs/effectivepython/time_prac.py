'''
time module usage

You mustn't use time module between different local times
because time module depends on host OS
and doesn't work properly against multiple local time.
Use datetime module to resolve this problems.
'''
from time import localtime, strftime
from time import mktime, strptime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print('time_str =', time_str)
# time_str = 2014-08-11 03:18:30

time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print('utc_now =', utc_now)
# utc_now = 1407694710.0

