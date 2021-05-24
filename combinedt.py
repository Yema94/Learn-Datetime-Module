from datetime import *

d = date(2021, 5, 20)
t = time(16,51)
dt = datetime.combine(d,t)
print(dt)



dt1 = datetime.today()
print(dt1)  
dt2 = datetime.combine(dt1.date(),dt1.time())
print(dt2)
