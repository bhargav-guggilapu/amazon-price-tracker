import smtplib
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
SENDER_EMAIL = 'pythontesterbhargav@gmail.com'
PASSWORD = os.environ["PASSWORD"]
url = "https://www.amazon.in/Apple-AirPods-Pro-2nd-Generation/dp/B0BDKD8DVD/ref=sr_1_2_sspa?crid=3OL9NDKR6BIJV&keywords=airpods+pro&qid=1665390221&qu=eyJxc2MiOiIzLjk0IiwicXNhIjoiMi44NiIsInFzcCI6IjQuMTMifQ%3D%3D&sprefix=%2Caps%2C226&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQkZFTVQxNUo3VkxHJmVuY3J5cHRlZElkPUEwMjAyNzU0UllWQ1I4VEFUUTJCJmVuY3J5cHRlZEFkSWQ9QTA0MDcxNzYxRkZCM1VITzBRVDNRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="    # input("Enter or Paste the URL:- ").strip()
RECEIVER_EMAIL = "alonefighter1210@gmail.com"   # input("Enter your email:- ").strip()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
itemName = driver.find_element(By.CSS_SELECTOR, '#productTitle').text.strip()
currentPrice = round(float(driver.find_element(By.CSS_SELECTOR, '.a-price-whole').text.replace(',', '')), 2)
actualPrice = round(float(driver.find_element(By.CSS_SELECTOR, '.a-text-price').text[1:].replace(',', '')), 2)
driver.quit()  #vchkuxurhzcpumcw
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=(f"Subject:Price track of {itemName}\n\nToday's price analysis for {itemName} is\r\nCurrent price is ₹{currentPrice}\r\nActual price is ₹{actualPrice}\r\nDecreased price is ₹{actualPrice - currentPrice}\r\nDiscount of {round(((actualPrice - currentPrice) / actualPrice) * 100, 2)}%").encode('utf-8'))
