import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

URL = 'https://www.afrihost.com/site/product/domain_registration'
browser.get(URL)
page = requests.get(URL)

form = browser.find_element_by_name('search-query')
form.clear()
form.send_keys(input('Type Domain name here...: '))
if form is not None:
    form_save = browser.find_element_by_id('domain-search-form')
    form_save.submit()
    try:
        element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "results-holder"))

    )
    finally:
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='domains-results')
        domains = results.find_all('div', class_='domains-holder left relative')

        for domains in domains:
            title = domains.find('h4', class_='section-title')
            dom = domains.find('d1', class_='domain-box')
            print('--------------------------------------')
            print('---------------SEARCHING--------------')
            print('--------------------------------------')
            print(title.text.strip())
            print(dom)
            print()
        browser.quit()
     