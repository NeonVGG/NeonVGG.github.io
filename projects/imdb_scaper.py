#imdb scraper
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
#print(soup.prettify)

#store movie title
titles = []
#store movie link
hrefs = []

td = soup.find_all('td',{'class':'titleColumn'})
for item in td:
    title = item.find('a')
    titles.append(title.text)
    href = item.find('a')
    hrefs.append(href.get('href'))

base_url = "https://www.imdb.com"

url_movies = []
for href in hrefs:
    url_temp = f'{base_url}{href}'
    url_movies.append(url_temp)

for movie in titles:
    print(movie)
for links in url_movies:
    response = requests.get(links)
    soup = BeautifulSoup(response.text,'lxml')
    div = soup.find('div',{'class':'subtext'}).find('time')
    #print(div.text)
    
