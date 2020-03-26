import urllib.request
import urllib.parse
import ssl
import gzip
import requests
import re


def crawlHtmlUrllib():
    # 模拟请求头（主要是设置cookie值）爬取登陆后网页的内容
    context = ssl._create_unverified_context()

    url = 'https://www.zhihu.com/people/liu-yu-xuan-46-99'
    headers = {
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '_zap=f23ba4f4-4663-4d47-8fac-87b0d8da14fc; d_c0="AMCVXwUXAhGPTljIVGkUr0aWnr7dqixV5Uw=|1584978028"; _ga=GA1.2.344562814.1584978030; _xsrf=mZXTQmZFYFlBN94GltooFvq3s0gVh9gL; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584978030,1584978749,1585195288; _gid=GA1.2.80910092.1585195288; capsion_ticket="2|1:0|10:1585195648|14:capsion_ticket|44:NTNkMjgwMjhiOGI5NGJjYzk5MGExNjg4MGVjZGM3MDk=|18877a664e1ca4bf44b9b23f2e1d7b9dd134c48ad71a63da0a722699a4a4051c"; z_c0="2|1:0|10:1585195652|4:z_c0|92:Mi4xZ3NxeEF3QUFBQUFBd0pWZkJSY0NFU1lBQUFCZ0FsVk5oSGhwWHdCRFEyYXpUREswaDJBc2dRWHUwdmxsUXdLZjZn|32b3879399975a220a43d5e3c1f9880d5df7ecf613180e835e5c7fcb2e1dc9ba"; _gat_gtag_UA_149949619_1=1; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585195675; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1585195675|1585195286',
                'referer': 'https://www.zhihu.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36}'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req, context=context)

    # gzip格式解压缩
    html = res.read().decode('utf-8')
    title = re.findall('<title data-react-helmet="true">(.*?)</title>', html)
    print(title[0])

def crawlHtmlRequests():
    url = 'https://www.zhihu.com/people/liu-yu-xuan-46-99'
    headers = {
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_zap=f23ba4f4-4663-4d47-8fac-87b0d8da14fc; d_c0="AMCVXwUXAhGPTljIVGkUr0aWnr7dqixV5Uw=|1584978028"; _ga=GA1.2.344562814.1584978030; _xsrf=mZXTQmZFYFlBN94GltooFvq3s0gVh9gL; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584978030,1584978749,1585195288; _gid=GA1.2.80910092.1585195288; capsion_ticket="2|1:0|10:1585195648|14:capsion_ticket|44:NTNkMjgwMjhiOGI5NGJjYzk5MGExNjg4MGVjZGM3MDk=|18877a664e1ca4bf44b9b23f2e1d7b9dd134c48ad71a63da0a722699a4a4051c"; z_c0="2|1:0|10:1585195652|4:z_c0|92:Mi4xZ3NxeEF3QUFBQUFBd0pWZkJSY0NFU1lBQUFCZ0FsVk5oSGhwWHdCRFEyYXpUREswaDJBc2dRWHUwdmxsUXdLZjZn|32b3879399975a220a43d5e3c1f9880d5df7ecf613180e835e5c7fcb2e1dc9ba"; _gat_gtag_UA_149949619_1=1; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585195675; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1585195675|1585195286',
        'referer': 'https://www.zhihu.com/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36}'}
    res = requests.get(url=url, headers=headers)
    html = res.content.decode('utf-8')

    title = re.findall('<title data-react-helmet="true">(.*?)</title>', html)
    print(title)

if __name__ == '__main__':
    crawlHtmlRequests()