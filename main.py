import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


load_dotenv("E:/Python/EnvironmentVariables/.env")
TWITTER_EMAIL = os.getenv("Email_Twitter")
TWITTER_PASSWORD = os.getenv("Password_Twitter")
GUARANTEED_MIN_SPEED = 3.4
ESTIMATED_UPLOAD = 1.0

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        self.result_id = "abc"
        self.ping = 0
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        print("Looking for button_consent")
        button_consent = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        button_consent.click()
        print("Looking for button_notification_close")
        found = False
        while not found:
            try:
                button_notification_close = self.driver.find_element_by_class_name("notification-dismiss")
                button_notification_close.click()
                found = True
            except:
                sleep(1)
        print("Looking for button_start_test")
        button_start_test = self.driver.find_element_by_class_name("js-start-test")
        button_start_test.click()
        # Get results
        # ===========
        sleep(30)
        print("Looking for result_id")
        #   Result ID
        found = False
        while not found:
            try:
                self.result_id = self.driver.find_element_by_class_name("result-item-id")\
                    .find_element_by_tag_name("a")
                # self.result_id.text doesn't print anything
                #   debug shows that .text does have the appropriate string value!!
                print("Result ID: ",
                      self.result_id.text,
                      self.result_id.get_attribute('href'))
                found = True
            except:
                sleep(1)
        #   Ping
        self.ping = self.driver.find_element_by_class_name("result-item-ping")\
            .find_element_by_class_name("ping-speed")
        print("Ping: ", self.ping.text, "ms")
        #   Download
        self.down = self.driver.find_element_by_class_name("result-item-download")\
            .find_element_by_class_name("download-speed")
        print("Download: ", self.down.text, "Mbps")
        #   Download
        self.up = self.driver.find_element_by_class_name("result-item-upload")\
            .find_element_by_class_name("upload-speed")
        print("Upload: ", self.up.text, "Mbps")

    def tweet_at_provider(self):
        pass


my_bot = InternetSpeedTwitterBot()
my_bot.get_internet_speed()
sleep(180)
my_bot.tweet_at_provider()






