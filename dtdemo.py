import time
import datetime

# prints in seconds
epochseconds = time.time()
print(epochseconds)

# output format: day month date hour:min:sec year
t = time.ctime(time.time())
print(t)

# output format : year-month-date hour:min:sec.milliseconds
dt = datetime.datetime.today()
print(dt)