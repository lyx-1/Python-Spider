import urllib.request
import urllib.parse
import requests
import json
import ssl


def fanyi_urllib(keyword):
    # urllib 版本

    context = ssl._create_unverified_context()
    data_dic = {'kw': keyword}
    url = 'https://fanyi.baidu.com/sug'
    headers = {'content-length': '8'}

    data = urllib.parse.urlencode(data_dic)
    # print(data)
    req = urllib.request.Request(url=url, data=bytes(data, encoding='utf-8'))
    res = urllib.request.urlopen(req, context=context)
    html = res.read().decode('utf-8')

    res_dic = json.loads(html)

    print(res_dic['data'][0]['v'])


def fanyi_requests(keyword):
    # requests 版本
    url = 'https://fanyi.baidu.com/sug'
    data = {'kw': keyword}

    res = requests.post(url=url, data=data)

    html = res.content.decode('utf-8')

    html_json = json.loads(html)
    print(html_json['data'][0]['v'])


if __name__ == '__main__':
    while True:
        x = input("请输入你想翻译的词语，q退出：")
        if x == 'q':
            break
        fanyi_requests(x)