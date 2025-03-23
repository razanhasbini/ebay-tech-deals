from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import os
from datetime import datetime


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)

url = "https://www.ebay.com/globaldeals/tech"
driver.get(url)


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(3)


products = driver.find_elements(By.CSS_SELECTOR, 'li.ebayui-dne-item-featured-card')


data = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for product in products:
    try:
        title = product.find_element(By.CSS_SELECTOR, 'h3').text.strip()
    except:
        title = "N/A"
    
    try:
        price = product.find_element(By.CSS_SELECTOR, '.dne-itemtile-price .first').text.strip()
    except:
        price = "N/A"

    try:
        original_price = product.find_element(By.CSS_SELECTOR, '.itemtile-price-strikethrough').text.strip()
    except:
        original_price = "N/A"
    
    try:
        shipping = product.find_element(By.CSS_SELECTOR, '.dne-itemtile-shipping').text.strip()
    except:
        shipping = "N/A"
    
    try:
        item_url = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        item_url = "N/A"

    data.append({
        'timestamp': timestamp,
        'title': title,
        'price': price,
        'original_price': original_price,
        'shipping': shipping,
        'item_url': item_url
    })


df = pd.DataFrame(data)


csv_file = 'ebay_tech_deals.csv'
if os.path.exists(csv_file):
    df.to_csv(csv_file, mode='a', header=False, index=False)
else:
    df.to_csv(csv_file, index=False)

print(f"Scraped {len(data)} items at {timestamp}")
driver.quit()
