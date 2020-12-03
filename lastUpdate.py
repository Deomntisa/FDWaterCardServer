import time

logFd = open("lastUpdate", "w")
logFd.write(str(time.time()))