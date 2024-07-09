import time
startTime=time.time()
for i in range(1,1000):
    print(i)
timeTaken=time.time()-startTime
print(timeTaken)
#This is not an effective way to calculate time, because it depends upon users computer
#Time complexity of algorithm cannot be determined during this aproach