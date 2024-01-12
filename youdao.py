from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Youdao:
    def __init__(self):
        # 创建一个Edge浏览器实例
        self.input_box = None
        self.drive = None
        options = webdriver.EdgeOptions()
        # 无界面
        options.add_argument('--headless')
        # 不关闭
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=options)
        # 打开有道翻译网站
        self.driver.get('https://fanyi.youdao.com/')
        # 等待页面加载完成，直到找到指定的元素
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/img[2]'))
        )
        # 点击该元素
        element.click()
        # 定位输入框并获取其引用
        self.input_box = self.driver.find_element(By.ID, 'js_fanyi_input')

    def send_keys(self, text):
        # 输入要翻译的内容
        self.input_box.send_keys(text)
        # # 定位翻译结果并获取其文本内容
        # element = WebDriverWait(driver, 10).until(
        # result_box = driver.find_element(By.XPATH, '//*[@id="js_fanyi_output_resultOutput"]/p/span')
        time.sleep(2)
        result_box = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="js_fanyi_output_resultOutput"]/p/span'))
        )
        result_text = result_box.text
        self.input_box.clear()
        return result_text

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
     youdao = Youdao()
     print(youdao.send_keys("你好"))
     print(youdao.send_keys('计算机'))
     youdao.quit()