from api import Pineapple

class SystemModule(object):
    def __init__(self, pineapple, name):
        super(SystemModule, self).__init__()
        self.pineapple = pineapple
    def request(self)