from module import Module

class Notifications(Module):
    def __init__(self, api):
        super(Notifications, self).__init__(api, 'notifications', True)
    def addNotification(self, message):
        return self.request('addNotification', {'message': message})
    def listNotifications(self):
        return self.request('listNotifications')
    def clearNotifications(self):
        return self.request('clearNotifications')
