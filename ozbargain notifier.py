from bs4 import BeautifulSoup
import requests
import notify2
import time

starttime=time.time()

notify2.init("ozbargain notifier")

def page_loader():
    url = requests.get("https://www.ozbargain.com.au/deals").text
    soup = BeautifulSoup(url, 'lxml')
    page_loader.title = soup.find("h2", class_="title").text
    page_loader.submitted = soup.find("div", class_="submitted").text

def deal_notifier():
    notification = notify2.Notification(page_loader.title,
                            page_loader.submitted,
                            "notification-message-im"   # Icon name
                            )
    notification.show()

last_deal = ""

while True:
    page_loader()
    if last_deal != page_loader.title:
        deal_notifier()
        print('"deal" found!')
    else:
        print("no new deals")
    last_deal = page_loader.title
    time.sleep(20.0)