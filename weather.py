from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567#.YFfPbGRKhro")

# page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567#.YFfPbGRKhro")

soup = BeautifulSoup(page.content, 'html.parser')

# sevenday = soup.find(id="seven-day-forecast")
# forecast = sevenday.find_all(class_="tombstone-container")

detailed = soup.find(id="detailed-forecast")
weekly = detailed.find_all(class_="forecast-label")
weather = detailed.find_all(class_="forecast-text")

# tonight = forecast[0]
# monday = forecast[1]

# img = tonight.find("img")
# desc = img['title']

# print(desc)

from gtts import gTTS
import os

"""
for i in range(len(forecast)):
    print(forecast[i].find("img")['title'])
    desc = forecast[i].find("img")['title']
    speech = gTTS(text = desc, slow = False)
    speech.save("desc.mp3")
    os.system("afplay desc.mp3")
"""

for i in range(len(weekly)):
    print(weekly[i].string + "." + " " + weather[i].string)
    desc = weekly[i].string + "." + " " + weather[i].string
    speech = gTTS(text = desc, lang = "en", tld = "ie", slow = False)
    speech.save("desc.mp3")
    os.system("afplay desc.mp3")
