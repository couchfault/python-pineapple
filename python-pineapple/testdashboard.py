from pineapple import *

#API_KEY = "98bc8c125c4f7ac897f7b18c6b53678331611a2d99d38cd281a3780c628009466353d4423a025e5d44be31a534b5580c09ba975e7dad9f3b8785a1033243218f"
API_KEY = "ee8ca88318b543abfb271eb6511578df91f8d46d70ca74c3eb8884555b3a1b63d8ad173a8c95e6281c086cae9cda799ca88da0041d257229f52e2f862617e47b"

def main():
    pineapple = api.Pineapple(API_KEY, url="http://localhost:1471/api/")
    dashboardTest = dashboard.Dashboard(pineapple)
    print "Overview data: "
    print repr(dashboardTest.getOverviewData())
    print "Landing page data: "
    print repr(dashboardTest.getLandingPageData())
    print "Bulletins: "
    print repr(dashboardTest.getBulletins())
    print "* Done *"

if __name__ == '__main__':
    main()