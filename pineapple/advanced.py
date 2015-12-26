from module import Module

class Advanced(Module):
    def __init__(self, api):
        super(Advanced, self).__init__(api, 'Advanced')
    def getResources(self):
        return self.request('getResources')
    def dropCaches(self):
        return self.request('dropCaches')
    def getUSB(self):
        return self.request('getUSB')
    def getFstab(self):
        return self.request('getFstab')
    def setFstab(self, fstab):
        return self.request('saveFstab', {'fstab', fstab})
    def getCSS(self):
        return self.request('getCSS')
    def setCSS(self, css):
        return self.request('saveCSS', {'css': css})
    def formatSDCard(self):
        return self.request('formatSDCard')
    def getFormatSDCardStatus(self):
        return self.request('formatSDCardStatus')
    def checkForUpgrade(self):
        return self.request('checkForUpgrade')
    def downloadUpgrade(self, version):
        return self.request('downloadUpgrade', {'version': version})
    def getUpgradeDownloadStatus(self, checksum):
        return self.request('getDownloadStatus', {'checksum': checksum})
    def performUpgrade(self):
        return self.request('performUpgrade')
    def getFirmareVersion(self):
        return self.request('getCurrentVersion')
