import os
from dotenv import load_dotenv
from selenium import webdriver, common
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
                    .find_element_by_tag_name("a").get_attribute('href')
                # self.result_id.text doesn't print anything
                #   debug shows that .text does have the appropriate string value!!
                print("Result ID: ", self.result_id)
                found = True
            except:
                sleep(1)
        #   Ping
        self.ping = self.driver.find_element_by_class_name("result-item-ping")\
            .find_element_by_class_name("ping-speed").text
        print("Ping: ", self.ping, "ms")
        #   Download
        self.down = self.driver.find_element_by_class_name("result-item-download")\
            .find_element_by_class_name("download-speed").text
        print("Download: ", self.down, "Mbps")
        #   Upload
        self.up = self.driver.find_element_by_class_name("result-item-upload")\
            .find_element_by_class_name("upload-speed").text
        print("Upload: ", self.up, "Mbps")

    def login_twitter(self):
        self.driver.get("https://twitter.com/login")
        sleep(3)
        # login_handle = self.driver.current_window_handle
        # print(login_handle)
        print("Looking for input_email")
        found = False
        while not found:
            try:
                input_email = self.driver.find_element_by_name("session[username_or_email]")
                input_email.send_keys(TWITTER_EMAIL)
                found = True
            except:
                sleep(1)
        input_password = self.driver.find_element_by_name("session[password]")
        input_password.send_keys(TWITTER_PASSWORD)
        print("Looking for button_login")
        button_login = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div"
        )
        button_login.click()

    def tweet_at_provider(self):
        # Get new page handle
        # home_handle = self.driver.window_handles[1]
        # print(home_handle)
        # Switch driver to new page
        # self.driver.switch_to.window(home_handle)
        sleep(3)
        print("Looking for button_tweet")
        found = False
        while not found:
            try:
                button_tweet = self.driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a"
                )
                button_tweet.click()
                found = True
            except:
                sleep(1)
        # Create message
        sleep(3)
        print("Looking for input_tweet")

        #
        # Project Abandoned - I am locked out of the Twitter account
        # Currently unable to get text into the Tweet box
        #

        input_tweet = self.driver.find_element_by_xpath(
            # "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div"
            "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div"
        )
        input_tweet.click()
        print("Looking for input_message")
        found = False
        while not found:
            try:
                input_tweet.send_keys(
                    f"Hey IP,\nWhy are my internet speeds so low?\n\n"
                )
                # input_message = self.driver.find_element_by_xpath(
                #     # "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div"
                #     "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div"
                # )
                # print(input_message.value_of_css_property())
                # input_message.send_keys(
                #     f"Hey IP,\nWhy are my internet speeds so low?\n\n"
                    # f"Result ID: {self.result_id}\n"
                    # f"Ping: {self.ping} ms\n"
                    # f"Download: {self.down} Mbps\n"
                    # f"Upload: {self.up} Mbps"
                # )
                found = True
            except common.exceptions.ElementNotInteractableException:
                print("selenium.common.exceptions.ElementNotInteractableException")
                sleep(1)
            except:
                print("Other exception")
                sleep(1)
        print("Looking for button_tweet")
        button_tweet = self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]"
        )
        button_tweet.click()


my_bot = InternetSpeedTwitterBot()
# my_bot.get_internet_speed()
my_bot.login_twitter()
my_bot.tweet_at_provider()





