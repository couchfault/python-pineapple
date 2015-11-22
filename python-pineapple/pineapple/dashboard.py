from api import Pineapple

class Dashboard(object):
    def __init__(self, pineapple):
        super(Dashboard, self).__init__()
        self.pineapple = pineapple
    def getOverviewData(self):
        return self.pineapple.moduleRequest('Dashboard', 'getOverviewData')
    def getLandingPageData(self):
        return self.pineapple.moduleRequest('Dashboard', 'getLandingPageData')
    def getBulletins(self):
        return self.pineapple.moduleRequest('Dashboard', 'getBulletins')