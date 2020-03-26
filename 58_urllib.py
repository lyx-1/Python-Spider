import urllib.request
import re
import ssl


def crawl_58():
    try:
        # urllib打开https连接的时候会验证ssl证书
        # 如果对方的ssl证书是自带的就会报错
        # 这时候可以选择取消全局证书验证 、 或者创建一个未验证的证书传入到urlopen
        context = ssl._create_unverified_context()

        url = "https://nj.58.com/tech/?key=python&cmcskey=python&final=1&jump=1&specialtype=gls"

        req = urllib.request.Request(url=url)

        res = urllib.request.urlopen(req,context=context)

        html = res.read().decode('utf-8')

        #print(len(html))

    except Exception as e:
        print(e.reason)


if __name__ == "__main__":
    crawl_58()
