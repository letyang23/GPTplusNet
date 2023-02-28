from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings("ignore")


def scraping_data(question):
    options = webdriver.ChromeOptions()
    options.headless = True
    url = "https://www.google.com/search?q=" + question
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

    data = []
    # border = browser.find_elements(By.CLASS_NAME, '')
    content = browser.find_elements(By.CLASS_NAME, 'VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf')
    for elements in content:
        print(elements.text)


scraping_data("What is tomorrow's weather going to be like?")
