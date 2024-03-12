import time
time = time.time()

ts = time

file = open("the-1Riddle.txt", 'w')
file.write("Time of run | ")
file.write(str(ts))
file.close()
