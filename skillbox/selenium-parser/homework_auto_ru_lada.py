import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()  # Open Chrome Browser
browser.set_window_size(1440, 900)

browser.get("https://auto.ru/")  # Open page https://auto.ru/ in Chrome Browser
browser.add_cookie({'name': 'autoru-visits-count', 'value': '3', 'path': '/', 'domain': '.auto.ru'})

# Find "All brands" element, and click it, because we don't know if the brand "LADA" will be in the preview
element_all_brands = browser.find_element(By.CLASS_NAME, "IndexMarks__show-all")
element_all_brands.click()
time.sleep(3)

# Find text "LADA" mark in class "IndexMarks__item-name" and click it
element_lada = browser.find_element(By.XPATH, "//div[@class='IndexMarks__item-name' and contains(text(), 'LADA')]")
element_lada.click()
time.sleep(3)

# Find element "On Credit" and click it
element_on_credit = browser.find_element(By.XPATH, "//input[@name='on_credit']")
element_on_credit.click()
time.sleep(3)

# Find element "Show offers" and click it
# element_show_offers = browser.find_element(By.XPATH, "//span[@class='Button__content']") # Captcha always appeared
element_show_offers = browser.find_element(By.XPATH, "//button[starts-with(@class, 'Button')]")
element_show_offers.click()
time.sleep(3)

# Find all div elements with class "ListingItem"
elements_listing = browser.find_elements(By.XPATH, "//div[@class='ListingItem']")
print(len(elements_listing))

# Find
#price = elements_listing.find_element(By.XPATH, "//div[@class='ListingItemPrice__content']").text

#for i in range(len(price)):
#    print (price[i])

for element in elements_listing:
    price = elements_listing[element].find_element(By.XPATH, "//div[@class='ListingItemPrice__content']").text
    #model = element.find_element(By.XPATH, "//a[ends-with(@class, 'ListingItemTitle__link')]").text
    print(price)

