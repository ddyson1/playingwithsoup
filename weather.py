from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567#.YFfPbGRKhro")

soup = BeautifulSoup(page.content, 'html.parser')

sevenday = soup.find(id="seven-day-forecast")
forecast = sevenday.find_all(class_="tombstone-container")

tonight = forecast[0]

img = tonight.find("img")
desc = img['title']

print(desc)

from gtts import gTTS
import os

speech = gTTS(text = desc, slow = False)

speech.save("desc.mp3")

os.system("afplay desc.mp3")
