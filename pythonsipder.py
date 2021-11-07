import requests
local_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
def search_on_sohu(word=None):
    # url = 'https://search.sohu.com/search/meta?keyword={word}'
    url = 'https://search.sohu.com/search/meta?keyword={word}&terminalType=pc&ip=111.196.241.191&city=北京市&spm-pre=smpc.content.search-box.1.1636289630746jEkCNDH&SUV=1634097561864tpmoxd&from=0&size=10&searchType=news&queryType=outside&queryId=1636289976191IOmC005&pvId=1636289976005XomYai6&refer=https://www.sohu.com/a/498268891_120900453&size=10&maxL=15&spm=&_=1636289976008'
    strhtml = requests.get(url.format_map(vars()),headers = local_headers)
    print(strhtml)
search_on_sohu("那些让人一眼万年的港风女神")


