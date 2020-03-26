import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json


def getPage(url):
    # 抓取网页
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    try:
        res = requests.get(url=url, headers=headers)
        if res:
            return res.text
        else:
            return None
    except RequestException as e:
        return None



def jiexiPage(content):
    # 解析内容
    soup = BeautifulSoup(content, 'html.parser')

    div_list = soup.find_all(name='div', attrs={'class': 'item'})
    for div in div_list:
        yield {
            'item': div.em.string,
            'name': div.find(name='span', attrs={'class': 'title'}).string,
            'score': div.find(name='span', attrs={'class': 'rating_num'}).string
        }


def writeFile(dict):
    # 写入文件
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(dict, ensure_ascii=False))
        f.write('\n')


if __name__ == '__main__':
    for offset in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(offset*25)
        html = getPage(url)
        if html:
            for item in jiexiPage(html):
                writeFile(item)
