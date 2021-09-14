from selenium import webdriver
from config import DRIVER_OPTIONS, DRIVER_PATH, URL_TO_XPATH

options = webdriver.ChromeOptions()
options.add_argument(DRIVER_OPTIONS)
driver = webdriver.Chrome(DRIVER_PATH, options=options)

for url, xpath in URL_TO_XPATH.items():
    try:
        driver.get(url)
        button = driver.find_element_by_xpath(xpath)
        button.click()
        print(f'Successfully bumped {url}!')
    except:
        print(f'Failed to Bump {url}')

input('Press any key to close...')
driver.quit()