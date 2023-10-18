import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 

# URL of the YouTube Music site
url = "https://music.youtube.com/"

# Send a GET request to the URL
response = requests.get(url)
driver = webdriver.Firefox()
driver.get("https://music.youtube.com/");


# html= driver.find_elements(By.CSS_SELECTOR , "button" );

# html[6].click()

time.sleep(3)
html = driver.find_element(By.CSS_SELECTOR, "ytmusic-carousel-shelf-renderer > div > ytmusic-carousel > div")
element_html = html.get_attribute('innerHTML');

soup  = BeautifulSoup(element_html , "html.parser");

songs = soup.select("ul > ytmusic-responsive-list-item-renderer")
Artists = []
Titles = []
Counts = []

for song in songs :
    title = song.select_one("ytmusic-responsive-list-item-renderer > div > div:first-of-type > yt-formatted-string").text.strip()
    artist = song.select_one("ytmusic-responsive-list-item-renderer > div > div:last-of-type > yt-formatted-string:first-of-type").text.strip()
    Artists.append(artist)
    Titles.append(title)
    Counts.append(1)

dict = {'Artist': Artists, 'Title': Titles, 'Count': Counts,}
df = pd.DataFrame(dict)

df.to_csv('Youtube.csv', index = False)