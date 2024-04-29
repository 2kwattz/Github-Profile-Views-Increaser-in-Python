import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import socks
import socket

# Set up a SOCKS proxy
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket

banner = pyfiglet.figlet_format("Github Views Increaser")
print(banner)
time.sleep(1)
print("Please enter account's username")
username = input()

timer_delay = int(input("Enter HTTP Request timer delay"))
views = int(input("Enter number of github views?"))

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Assuming you have Chrome WebDriver installed.
driver = webdriver.Chrome(options=chrome_options)

# Setting up user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

view_count = 0

try:
 for _ in range(views):
   view_count = view_count + 1
   driver.get(f"https://github.com/{username}")
   print(f" Current {view_count}")

   time.sleep(timer_delay)

     
except Exception as e:
   print(e)
   driver.quit()

