import os
import requests
import telegram
from bs4 import BeautifulSoup
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_alert(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def check_asics():
    url = "https://www.asics.co.in/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    if "kinetic fluent" in response.text.lower():
        send_alert("🟢 Kinetic Fluent might be listed on Asics India! Check: https://www.asics.co.in/")

if __name__ == "__main__":
    while True:
        check_asics()
        time.sleep(3600)