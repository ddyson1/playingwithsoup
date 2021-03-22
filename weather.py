from bs4 import BeautifulSoup
import requests

cities = ["Boston", "NYC", "Weston"]
print(cities)

city = input("Pick a city from the array above to hear the weekly forecast for that city: ")

if city == cities[0]:
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567#.YFfPbGRKhro")
elif city == cities[1]:
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YFgJXmRKhro")
elif city == cities[2]:
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.2244&lon=-73.383")
else:
    print("The city you entered is not on the list. Defaulting to Boston, MA")
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
    speech = gTTS(text = desc, slow = False)
    speech.save("desc.mp3")
    os.system("afplay desc.mp3")
