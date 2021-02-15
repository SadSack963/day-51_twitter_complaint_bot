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
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button_consent = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        button_consent.click()
        button_notification_close = self.driver.find_element_by_css_selector("notification-dismiss close-btn")
        button_notification_close.click()
        button_start_test = self.driver.find_element_by_css_selector("js-start-test test-mode-multi")
        button_start_test.click()

        pass

    def tweet_at_provider(self):
        pass


my_bot = InternetSpeedTwitterBot()
my_bot.get_internet_speed()
sleep(180)
my_bot.tweet_at_provider()






