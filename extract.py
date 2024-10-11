import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Safari()

url = 'https://codis.cwa.gov.tw/StationData'
driver.get(url)

time.sleep(10)


driver.maximize_window()

time.sleep(5)

button = driver.find_element(By.XPATH, '//*[@id="switch_display"]/button[2]')
button.click()

checkbox1 = driver.find_element(By.XPATH, '//*[@id="auto_C1"]')
checkbox1.click()
checkbox2 = driver.find_element(By.XPATH, '//*[@id="auto_C0"]')
checkbox2.click()
checkbox3 = driver.find_element(By.XPATH, '//*[@id="agr"]')
checkbox3.click()

button = driver.find_element(By.XPATH, '//*[@id="station_filter"]/div/section/ul/li[6]/div/div[2]/div/button[1]')
#button.click()

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', class_='v-table-content')
#print(table)

data = []

rows = table.find_all('tr', class_='')
for row in rows:
    cells = row.find_all('td')
    cell_texts = [cell.get_text(strip = True) for cell in cells]
    data.append(cell_texts)

csv_filename = '測站__.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
