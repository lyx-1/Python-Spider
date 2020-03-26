import requests
from bs4 import BeautifulSoup

def getPage(url):
    res = requests.get(url=url)

    if res.text:
        return res.text
    else:
        return None

def getImageUrl(content):
    soup = BeautifulSoup(content, 'html.parser')

    img_list = soup.find_all(name='img', attrs={'width': '220', 'height': '220'})
    img_url_list = []
    # 延迟绑定
    for img in img_list:
        if 'src' in img.attrs:
            # print(img)
            img_url_list.append('https:' + img.attrs['src'])
        else:
            img_url_list.append('https:' + img.attrs['data-lazy-img'])
    return img_url_list


def writeImg(img_url_list):
    for img_url in img_url_list:
        with requests.get(img_url, stream=True) as r:
            with open(str(img_url_list.index(img_url)) + '.png', 'wb') as f:
                for chunk in r:
                    f.write(chunk)


if __name__ == '__main__':
    url = 'https://list.jd.com/list.html?cat=9987,653,655'
    html = getPage(url)
    img_url_list = getImageUrl(html)
    writeImg(img_url_list)