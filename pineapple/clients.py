from module import Module

class Clients(Module):
    def __init__(self, api):
        super(Clients, self).__init__(api, 'Clients')
    def getClientData(self):
        return self.request('getClientData')
    def kickClient(self, mac):
        return self.request('kickClient', {'mac': mac})
