# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# https://blog.csdn.net/ever_peng/article/details/90547299

class VerificationCode:
    def __init__(self):
        # self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.find_element = self.driver.find_element_by_css_selector

    def get_pictures(self):
        self.driver.get('https://auth.mingyuanyun.com/')  # 打开登陆页面
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#valiCode'))
        )
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        img = self.find_element('#valiCode')  # 验证码元素位置
        time.sleep(1)
        location = img.location
        print(location)
        size = img.size  # 获取验证码的大小参数
        print(size)
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        im = Image.open('pictures.png')
        im_obj = im.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        im_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return im_obj


if __name__ == '__main__':
    a = VerificationCode()
    a.get_pictures()


# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://auth.mingyuanyun.com/")
# driver.find_element(By.ID,"Username").clear()
# driver.find_element(By.ID,"Username").send_keys("wup06")
# driver.find_element(By.ID,"Username").send_keys("Password")
