from module import Module

class Tracking(Module):
    def __init__(self, api):
        super(Tracking, self).__init__(api, 'Tracking')
    def getScript(self):
        return self.request('getScript')
    def setScript(self, script):
        return self.request('saveScript', {'trackingScript': script})
    def getTrackingList(self):
        return self.request('getTrackingList')
    def addMac(self, mac):
        return self.request('addMac', {'mac': mac})
    def removeMac(self, mac):
        return self.request('removeMac', {'mac': mac})
    def clearMacs(self):
        return self.request('clearMacs')
