from datetime import date
import time

startTime = time.perf_counter()
ldates = []

d1 = date(2016, 9, 26)
d2 = date(2016, 3, 26)
d3 = date(2016, 4, 24)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort(reverse=True)
#ime.sleep(3)
for i in ldates:
    print(i)

endTime = time.perf_counter()
print("Execution Time: ", endTime-startTime)