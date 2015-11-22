from api import Pineapple

class Notifications(object):
    def __init__(self, pineapple):
        super(Notifications, self).__init__()
        self.pineapple = pineapple
    def addNotification(self, message):
        self.pineapple.systemRequest('notifications', 'addNotification', {'message': message})
    def listNotifications(self):
        return self.pineapple.systemRequest('notifications', 'listNotifications')
    def clearNotifications(self):
        return self.pineapple.systemRequest('notifications', 'clearNotifications')