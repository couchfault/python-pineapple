from module import Module

class Dashboard(Module):
    def __init__(self, api):
        super(Dashboard, self).__init__(api, 'Dashboard')
    def getOverviewData(self):
        return self.request('getOverviewData')
    def getLandingPageData(self):
        return self.request('getLandingPageData')
    def getLandingPageStats(self):
        return self.getLandingPageData()
    def getBulletins(self):
        return self.request('getBulletins')
