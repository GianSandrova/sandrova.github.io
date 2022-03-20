from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "D:\ASUS\Documents\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/year-end/hot-100-songs/")

songlist = []
now = datetime.now()
i = 1
while i<=100:
    for lagu in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
        print(lagu.text.split("\n"))
        for img in lagu.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            i = i+1
            songlist.append(
                {"No": lagu.text.split("\n")[0],
                "Song": lagu.text.split("\n")[1],
                "Singer": lagu.text.split("\n")[2],
                "Image": img.get_attribute("src"),
                "Scrapping_Time": now.strftime("%d %B %Y %H:%M:%S")
                }
            )
hasil_scraping = open("hasilscraping.json", "w")
json.dump(songlist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()