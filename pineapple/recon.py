from module import Module

class Recon(Module):
    def __init__(self, api):
        super(Recon, self).__init__(api, 'Recon')
    def getScanStatus(self, scanId, scanType):
        return self.request('getScanStatus', {'scan': {'scanID': scanId, 'scanType': scanType}})
    def startScan(self, scanType, scanDuration):
        return self.request('startScan', {'scanType': scanType, 'scanDuration': scanDuration})
