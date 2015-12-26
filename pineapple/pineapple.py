from api import API
from . import modules

# from pineapple import *;p=pineapple.Pineapple('7a0685064eb99de1f89a73cd403f13fdaadc42cff8624d8b6d5389f1fc19b8bbe2f960b8f70e38b49b4c581029ad939c967e44ce52ededd82a67bc6ca188d21e')
class Pineapple(object):
    def __init__(self, apiKey, apiUrl = None):
        super(Pineapple, self).__init__()
        self.api = API(apiKey, apiUrl)
        self.modules = {}
        self._pineappleModule = __import__('pineapple')
        for moduleName in modules:
            moduleClass = self._pineappleModule.__dict__[moduleName].__dict__[moduleName.title()]
            self.modules[moduleName] = moduleClass(self.api)
    def loadModule(self, moduleClass):
        self.modules[moduleClass.__name__] = moduleClass(self.api)
    def getModule(self, module):
        return self.modules[module]
