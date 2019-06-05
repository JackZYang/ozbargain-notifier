from bs4 import BeautifulSoup
import requests
import notify2
import time

starttime=time.time()

notify2.init("ozbargain notifier")

def page_loader():
    url = requests.get("https://www.ozbargain.com.au/deals").text
    soup = BeautifulSoup(url, 'lxml')
    page_loader.title = soup.find("h2", class_="title")
    page_loader.link = "https://www.ozbargain.com.au/" + page_loader.title.a["href"]

def deal_notifier():
    notification = notify2.Notification(page_loader.title.text,
                            str(page_loader.link),
                            )
    notification.show()

last_deal = ""

while True:
    page_loader()
    if last_deal != page_loader.title.text:
        deal_notifier()
        print('"deal" found!')
    else:
        print("no new deals")
    last_deal = page_loader.title.text
    time.sleep(20.0)