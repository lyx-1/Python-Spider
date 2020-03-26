import requests
import re
import ssl


def crawl_58(position):
    try:
        key = {'key': position, 'cmcskey': position, 'final': '1', 'jump': '1', 'specialtype': 'job'}


        url = "https://nj.58.com/tech/"

        # req = urllib.request.Request(url=url)

        res = requests.get(url, params=key)

        html = res.content.decode('utf-8')

        # print(len(html))
        pat = '<span class="address"> (.*?) </span>  \| <span class="name">(.*?)</span>'

        res_list = re.findall(pat, html)

        for result in res_list:
            print(result[0] + result[1])
        # print(len(res_list))

    except Exception as e:
        if hasattr(e, 'reason'):
            print(e.reason)


if __name__ == "__main__":
    crawl_58("c")