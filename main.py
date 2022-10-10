import smtplib
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

SENDER_EMAIL = 'pythontesterbhargav@gmail.com'
PASSWORD = os.environ["PASSWORD"]
url = "https://www.amazon.in/Apple-AirPods-Pro-2nd-Generation/dp/B0BDKD8DVD/ref=sr_1_2_sspa?crid=3OL9NDKR6BIJV&keywords=airpods+pro&qid=1665390221&qu=eyJxc2MiOiIzLjk0IiwicXNhIjoiMi44NiIsInFzcCI6IjQuMTMifQ%3D%3D&sprefix=%2Caps%2C226&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQkZFTVQxNUo3VkxHJmVuY3J5cHRlZElkPUEwMjAyNzU0UllWQ1I4VEFUUTJCJmVuY3J5cHRlZEFkSWQ9QTA0MDcxNzYxRkZCM1VITzBRVDNRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="   # input("Enter or Paste the URL:- ").strip()
RECEIVER_EMAIL = "alonefighter1210@gmail.com"   # input("Enter your email:- ").strip()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

driver = webdriver.Chrome(options = options)
driver.set_page_load_timeout(30)
driver.get(url)

itemName = driver.find_element(By.CSS_SELECTOR, '#productTitle').text.strip()
currentPrice = round(float(driver.find_element(By.CSS_SELECTOR, '.a-price-whole').text.replace(',', '')), 2)
actualPrice = round(float(driver.find_element(By.CSS_SELECTOR, '.a-text-price').text[1:].replace(',', '')), 2)

driver.quit()  #vchkuxurhzcpumcw

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=(f"Subject:Price track of {itemName}\n\nToday's price analysis for {itemName} is\r\nCurrent price is ₹{currentPrice}\r\nActual price is ₹{actualPrice}\r\nDecreased price is ₹{actualPrice - currentPrice}\r\nDiscount of {round(((actualPrice - currentPrice) / actualPrice) * 100, 2)}%").encode('utf-8'))
