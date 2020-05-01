from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class InstaBot:
    """docstring for InstaBot"""

    def __init__(self, username, password):
        super(InstaBot, self).__init__()
        mobile_emulation = {
            "deviceMetrics": {"width": 460, "height": 840, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) \
            AppleWebKit/535.19 (KHTML, like Gecko) \
            Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options = Options()
        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath(
            '//button[contains(text(), \'Войти\')]').click()
        sleep(2)
        self.__insert_keys(username, password)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Не сейчас')]").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Отмена')]").click()
        sleep(3)

    def like_last_photo_in_profile(self):
        self.__back_to_profile()
        # xpath to first photo
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div[1]/div[1]').click()
        sleep(3)
        self.__put_like_in_detail_photo()
        self.__back_to_profile()
        sleep(4)
        self.driver.close()

    def send_hello(self, nickname=str()):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[2]').click()
        sleep(4)
        self.driver.find_element_by_xpath(
            '//input[@type=\'search\']').send_keys(nickname)
        sleep(3)
        self.driver.get("https://instagram.com/{}/".format(nickname))
        sleep(3)
        self.driver.find_element_by_xpath(
            '//button[contains(text(), "Отправить сообщение")]').click()
        sleep(4)
        self.driver.find_element_by_xpath(
            '//textarea').send_keys('Hello, it\'s me! Can u hear me?')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//button[contains(text(), \'Отправить\')]').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div[1]/header/div/div[1]').click()
        sleep(2)
        self.__back_to_lenta()
        sleep(5)
        self.driver.close()

    def __insert_keys(self, username, password):
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        sleep(4)

    def __back_to_profile(self):
        self.driver.find_element_by_xpath(
            '//a[@href=\'/{}/\']'.format(self.username)).click()
        sleep(2)

    def __put_like_in_detail_photo(self):
        for i in range(0, 2):
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div[1]').click()
        sleep(3)

    def __back_to_lenta(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[1]').click()


if __name__ == '__main__':
    bot = InstaBot('login', 'password')
    # bot.like_last_photo_in_profile()
    # bot.send_hello('username')
