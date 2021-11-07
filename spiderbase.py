from fake_useragent import UserAgent
class SpiderBase:
    def headers(self):
        ua = UserAgent()
        headers = {'User-Agent':{ua.ie},}
        # headers['User-Agent'] = ua.ie
        print(headers)
        return headers
    def params(self):
        params = []
        return params
    def uri(self):
        return ''

class Sohu(SpiderBase):
    def uri():
        return 'https://search.sohu.com/search/meta'


base = SpiderBase()
base.headers()