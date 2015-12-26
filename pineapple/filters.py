from module import Module

class Filters(Module):
    def __init__(self, api):
        super(Filters, self).__init__(api, 'Filters')
    def getClientData(self):
        return self.request('getClientData')
    def getSSIDData(self):
        return self.request('getSSIDData')
    def toggleClientMode(self, allow):
        mode = 'Allow' if enabled else 'Disallow'
        return self.request('toggleClientMode', {'mode': mode})
    def toggleSSIDMode(self, allow):
        mode = 'Allow' if enabled else 'Disallow'
        return self.request('toggleSSIDMode', {'mode': mode})
    def addClient(self, mac):
        return self.request('addClient', {'mac': mac})
    def removeClient(self, mac):
        return self.request('removeClient', {'mac': mac})
    def addSSID(self, ssid):
        return self.request('addSSID', {'ssid': ssid})
    def removeSSID(self, ssid):
        return self.request('removeSSID', {'ssid': ssid})
