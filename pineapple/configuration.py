import re
from module import Module

class Configuration(Module):
    def __init__(self, api):
        super(Configuration, self).__init__(api, 'Configuration')
        self.timezoneRegex = re.compile(r'^(GMT[+-](([0-9]$)|(1[0-2]$)))|(UTC$)')
    def getCurrentTimezone(self):
        return self.request('getCurrentTimezone')
    def getLandingPageData(self):
        return self.request('getLandingPageData')
    def setLandingPageData(self, data):
        return self.request('saveLandingPageData', {'landingPageData': data})
    def changePassword(self, oldPassword, newPassword):
        return self.request('changePassword', {'newPassword': newPassword, 'newPasswordRepeat': newPassword, 'oldPassword': oldPassword})
    def changeTimezone(self, timezone):
        if (self.timezoneRegex.match(timezone)):
            return self.request('changeTimezone', {'timezone': timezone})
        else:
            raise ValueError('Invalid Timezone: ' + timezone)
    def resetPineapple(self):
        return self.request('resetPineapple')
    def rebootPineapple(self):
        return self.request('rebootPineapple')
    def getLandingPageStatus(self):
        return self.request('getLandingPageStatus')
    def enableLandingPage(self):
        return self.request('enableLandingPage')
    def disableLandingPage(self):
        return self.request('disableLandingPage')
    
