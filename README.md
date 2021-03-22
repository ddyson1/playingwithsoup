## playingwithsoup

> pip3 install virtualenv

change directory into project folder

>cd playingwithsoup/

activate your virtual environment to keep things clean

>virtualenv venv

>source venv/bin/activate

(venv) should appear

install your dependencies for venv

>pip3 install beautifulsoup4

>pip3 install lxml

>pip3 install requests

>pip3 install gTTS

run the scripts!

>python3 soup.py

soup.py was written to extract every news headline from the EL PAÍS homepage

>python3 weather.py

weather.py was written to interpret Boston weather data from the National Weather Service, save Tonight's forecast description to an mp3 file and then use Google's Text To Speech (gTTS) to speak aloud Tonight's weather (in Boston!!)
