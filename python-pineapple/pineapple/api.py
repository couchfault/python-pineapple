import requests
import json
import urllib

class Pineapple(object):
    def __init__(self, apiToken, url='http://172.16.42.1:1471'):
        super(Pineapple, self).__init__();
        self.apiToken = apiToken
        self.url = url
        self.userAgent = "Pynapple"
        self.headers = {'User-Agent': self.userAgent, 'Content-Type': 'application/json', 'Accept': 'text/json'}
    def systemRequest(self, module, action, args=None):
        requestObject = {'apiToken': self.apiToken, 'system': module, 'action': action}
        if args:
            requestObject.update(args)
        payload = json.dumps(requestObject)
        resp = requests.post(self.url, data=payload, headers=self.headers)
        try:
            return json.loads(resp.text)
        except ValueError, e:
            print "Error decoding: "+repr(resp.text)
            print e
    def moduleRequest(self, module, action, args=None):
        requestObject = {'apiToken': self.apiToken, 'module': module, 'action': action}
        if args:
            requestObject.update(args)
        payload = json.dumps(requestObject)
        resp = requests.post(self.url, data=payload, headers=self.headers)
        try:
            return json.loads(resp.text)
        except ValueError, e:
            print "Error decoding: "+repr(resp.text)
            print e