import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, x):
        #super().append(self,x)
        super(LoggableList,self).append(x)
        self.log(x)


loglist = LoggableList()
log = Loggable()
print(loglist)
loglist.append(5)
print(loglist)
print(log.log('wow'))
