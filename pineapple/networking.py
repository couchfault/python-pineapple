from module import Module

class Networking(Module):
    def __init__(self, api):
        super(Networking, self).__init__(api, 'Networking')
    def getRoutingTable(self):
        return self.request('getRoutingTable')
    def restartDNS(self):
        return self.request('restartDNS')
    def updateRoute(self, routeInterface, routeIP):
        return self.request('updateRoute', {'routeInterface': routeInterface, 'routeIP': routeIP})
    def getAdvancedData(self):
        return self.request('getAdvancedData')
    def setHostname(self, hostname):
        return self.request('setHostname', {'hostname': hostname})
    def resetWirelessConfig(self):
        return self.request('resetWirelessConfig')
    def getInterfaceList(self):
        return self.request('getInterfaceList')
    def saveAPConfig(self, apConfig):
        return self.request('saveAPConfig', {'apConfig': apConfig})
    def getAPConfig(self):
        return self.request('getAPConfig')
    def getMacData(self):
        return self.request('getMACData')
    def setMac(self, mac):
        return self.request('setMac', {'mac': mac})
    def setRandomMac(self):
        return self.request('setRandomMac')
    def resetMac(self):
        return self.request('resetMac')
    def scanForNetworks(self, interface):
        return self.request('scanForNetworks', {'interface': interface})
    def getClientInterfaces(self):
        return self.request('getClientInterfaces')
    def connectToAP(self, interface, security, password = ''):
        return self.request('connectToAP', {'interface': interface, security: security, key: password})
    def checkConnection(self):
        return self.request('checkConnection')
    def disconnect(self, interface):
        return self.request('disconnect', {'interface': interface})
