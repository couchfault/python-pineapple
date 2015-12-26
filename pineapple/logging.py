from module import Module

class Logging(Module):
    def __init__(self, api):
        super(Logging, self).__init__(api, 'Logging')
    def getSyslog(self):
        return self.request('getSyslog')
    def getDmesg(self):
        return self.request('getDmesg')
    def getReportingLog(self):
        return self.request('getReportingLog')
    def getPineapLog(self):
        return self.request('getPineapLog')
    def clearPineapLog(self):
        return self.request('clearPineapLog')
