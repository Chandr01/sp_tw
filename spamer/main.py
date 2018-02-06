from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random

messages = ['for the test']
user = ['@Lox']

def open_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    browser = webdriver.Firefox(profile)
    browser.get('https://twitter.com/login')
    return browser

def login(browser):
    email = browser.find_elements_by_class_name('email-input')
    email[1].clear()
    email[1].send_keys('evgeniychan@gmail.com')
    password = browser.find_element_by_class_name('js-password-field')
    password.clear()
    password.send_keys('32167chan')
    button = browser.find_elements_by_class_name('submit')
    button[1].click()
    sleep(5)

def tweet(browser, messages, user):
    text = '{} {}'.format(user[0], messages[0])
    tweet = browser.find_element_by_id('global-new-tweet-button')
    tweet.click()
    sleep(3)

    for i in text:
        actions = ActionChains(browser)
        actions.send_keys(i)
        actions.perform()
        sleep(random.uniform(0.05, 0.2))
    sleep(2)
    # ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()


def main():
    browser = open_driver()

    login(browser)
    tweet(browser, messages, user)





if __name__=='__main__':
    main()