import json
from module import Module

class Reporting(Module):
    def __init__(self, api):
        super(Reporting, self).__init__(api, 'Reporting')
    def getReportingConfiguration(self):
        return self.request('getReportingConfiguration')
    def setReportingConfiguration(self, storeReport, sendEmail, reportInterval, generateReport):
        return self.request('setReportingConfiguration', {'config': json.dumps({'storeReport': storeReport, 'sendReport': sendEmail, 'interval': reportInterval, 'generateReport': generateReport})})
    def getReportContents(self):
        return self.request('getReportContents')
    def getEmailConfiguration(self):
        return self.request('getEmailConfiguration')
    def setEmailConfiguration(self, fromAddr, to, server, port, domain, username, password, tls, starttls):
        return self.request('setEmailConfiguration', {'config': json.dumps({'from': fromAddr, 'to': to, 'server': server, 'port': port, 'domain': domain, 'username': username, 'password': password, 'tls': tls, 'starttls': starttls})})
    def setReportContents(self, pineAPLog, clearLog, siteSurvey, siteSurveyDuration, client, tracking):
        return self.request('setReportContents', {'pineAPLog': pineAPLog, 'clearLog': clearLog, 'siteSurvey': siteSurvey, 'siteSurveyDuration': siteSurveyDuration, 'client': client, 'tracking': tracking})
