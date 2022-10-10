import requests
from bs4 import BeautifulSoup
import smtplib
import os
SENDER_EMAIL = 'pythontesterbhargav@gmail.com'
PASSWORD = os.environ["PASSWORD"]
# url = input("Enter or Paste the URL:- ").strip()
# RECEIVER_EMAIL = input("Enter your email:- ").strip()
url = "https://www.amazon.in/Apple-AirPods-Pro-2nd-Generation/dp/B0BDKD8DVD/ref=sr_1_2_sspa?crid=3OL9NDKR6BIJV&keywords=airpods+pro&qid=1665390221&qu=eyJxc2MiOiIzLjk0IiwicXNhIjoiMi44NiIsInFzcCI6IjQuMTMifQ%3D%3D&sprefix=%2Caps%2C226&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQkZFTVQxNUo3VkxHJmVuY3J5cHRlZElkPUEwMjAyNzU0UllWQ1I4VEFUUTJCJmVuY3J5cHRlZEFkSWQ9QTA0MDcxNzYxRkZCM1VITzBRVDNRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
RECEIVER_EMAIL = "alonefighter1210@gmail.com"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
itemName = soup.find("span", {"id": "productTitle"}).get_text().strip()
currentPrice = float(soup.find("span", {"class": "a-offscreen"}).get_text()[1:].replace(',', ''))
actualPrice = float(soup.find("span", {"class": "a-text-price"}).get_text()[1:].rpartition('₹')[0].replace(',', ''))
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=(f"Subject:Price track of {itemName}\n\nToday's price analysis for {itemName} is\r\nCurrent price is ₹{currentPrice}\r\nActual price is ₹{actualPrice}\r\nDecreased price is ₹{actualPrice - currentPrice}\r\nDiscount of {round(((actualPrice - currentPrice) / actualPrice) * 100, 2)}%").encode('utf-8'))