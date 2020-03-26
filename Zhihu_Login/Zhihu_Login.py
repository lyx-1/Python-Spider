import urllib.parse
import requests
import hmac
import hashlib
import re
import json
import base64
import threading
from PIL import Image
import matplotlib.pyplot as plt
import execjs
import time
import os


def get_xsrf(headers):
    url = 'https://www.zhihu.com/'
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    xsrf = res.cookies['_xsrf']
    # print(xsrf)
    return xsrf


def build_signature(grantType, clientId, source, timestamp):
    h = hmac.new(bytes("d1b964811afb40118a12068ff74a12f4", encoding='utf-8'), bytes("",encoding='utf-8'), hashlib.sha1)
    h.update(bytes(grantType+clientId+source+str(timestamp), encoding='utf-8'))
    return h.hexdigest()


def get_captcha(lang, headers):
    if lang == 'cn':
        url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=cn"
    else:
        url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"

    res = requests.get(url=url, headers=headers)
    cookies = res.cookies
    flag = re.findall("true", res.text)
    captcha = ""

    if flag:
        captcha_res = requests.put(url=url, cookies=cookies, headers=headers)
        captcha_json = json.loads(captcha_res.text)
        captcha_image = captcha_json['img_base64'].replace("\n", "")

        with open("./Zhihu_Login/captcha.png", 'wb') as image:
            image.write(base64.b64decode(captcha_image))

        if lang == 'cn':
            image = Image.open("./Zhihu_Login/captcha.png")
            plt.imshow(image)
            point_list = plt.ginput(7)

            captcha_dic = {'image_size': [200, 44], 'input_points': []}
            for point in point_list:
                captcha_dic['input_points'].append([point[0]/2,point[1]/2])

            captcha = json.dumps(captcha_dic)
        elif lang == 'en':
            image = Image.open("./Zhihu_Login/captcha.png")
            image_thread = threading.Thread(target=image.show)
            image_thread.setDaemon(True)
            image_thread.start()
            captcha = input("请输入图片里的验证码：")
        r = requests.post(url, headers=headers, data={"input_text": captcha}, cookies=cookies)
        print(r.text)

    # print(captcha)
    return captcha, cookies


def encrypt_data(data_dic):
    with open('./Zhihu_Login/encrypt.js', 'r') as f:
        js = execjs.compile(f.read())
        os.environ['EXEJS_RUNTIME'] = "Node"
        os.environ["NODE_PATH"] = r"/usr/local/bin/node"

        data = js.call(u'Q', urllib.parse.urlencode(data_dic))
        print(data)
        return data


if __name__ == '__main__':
    timestamp = int(1000*time.time())
    data_dict = {
        "captcha": "",
        "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
        "grant_type": "password",
        "lang": "en",
        "password": "lbiaoche123",
        "ref_source": "homepage",
        "signature": "",
        "source": "com.zhihu.web",
        "timestamp": timestamp,
        "username": "15576379437",
        "utm_source": "",
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    xsrf = get_xsrf(headers)

    data_dict['captcha'], cookies = get_captcha('cn', headers)
    data_dict['signature'] = build_signature(data_dict['grant_type'], data_dict['client_id'], data_dict['source'], data_dict['timestamp'])

    data = encrypt_data(data_dict)

    header = {
        "content-type": "application/x-www-form-urlencoded",
        # "Referer":"https://www.zhihu.com/signin",
        'x-zse-83': '3_1.1',
        "x-xsrftoken": xsrf,
    }
    headers.update(header)
    print(data_dict['signature'])
    print(headers['x-xsrftoken'])
    sign_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
    res = requests.post(url=sign_url, headers=headers, data=data, cookies=cookies)
    print(json.loads(res.content.decode('utf-8')))
