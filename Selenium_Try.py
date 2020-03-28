from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def getPage(offset):
    try:
        url = 'https://s.taobao.com/search?q=ipad'
        driver.get(url)
        input("完成验证？")
        WebDriverWait(driver, 10)

        # 拿到输入.. 按钮.. 输入相应页号.. 解析..
        input = expected_conditions.presence_of_element_located(By.CSS_SELECTOR, " ")
        # .......
    except TimeoutException as e:
        getPage(offset)


def main():
    # getPage(1)
    driver.close()


if __name__ == '__main__':
    main()