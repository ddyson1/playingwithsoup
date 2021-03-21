import requests

page = requests.get("https://english.elpais.com/")
# http://127.0.0.1:8000/screen/add_stock.html

# print(page.status_code)
# print(page.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

coverpage = soup.find_all('h2')
# soup.find_all('h2', class_='someclass')

# len(soup.find_all('h2') counts the amount of h2 tags in page
for i in range(len(soup.find_all('h2'))):
    print(i + 1)
    print(coverpage[i].get_text())

# soup.find_all('p')[0].get_text()
# print(soup.prettify())

# print(soup.title.string)
# print(soup.find_all('td'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())
