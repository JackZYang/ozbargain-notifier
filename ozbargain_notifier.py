from bs4 import BeautifulSoup
import requests
import notify2
import time

starttime = time.time()

notify2.init("ozbargain notifier")

def page_loader():
    url = requests.get("https://www.ozbargain.com.au/deals").text
    soup = BeautifulSoup(url, 'lxml')
    page_loader.titles = soup.find_all("h2", class_="title")
    page_loader.latest = page_loader.titles[0]

def deal_notifier():
    if last_deal:
        try:
            index_last = page_loader.titles.index(last_deal)
        except:
            index_last = 1
        print(index_last)
    else:
        index_last = 1
    for i in range(index_last):
            notification = notify2.Notification(page_loader.titles[i].text,
                                str("https://www.ozbargain.com.au/" + page_loader.titles[i].a["href"]),
                                )
            notification.show()
            time.sleep(5)

last_deal = ""

while True:
    page_loader()
    if last_deal != page_loader.latest:
        print('"deal" found!')
        deal_notifier()
    else:
        print("no new deals")
    last_deal = page_loader.latest
    time.sleep(180)