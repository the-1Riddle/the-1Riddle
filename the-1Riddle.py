import time

localtime = time.asctime( time.localtime(time.time()) )

execTime = localtime

file = open("the-1Riddle.txt", 'w')
file.write("Time of run : ")
file.write(str(execTime))
file.close()
