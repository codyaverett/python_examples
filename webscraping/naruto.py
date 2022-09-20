#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup


req = urllib.request.Request(
    url='https://www.animefillerlist.com/shows/naruto-shippuden',
    # Trick the websites into thinking we are a browser
    headers={'User-Agent': 'Mozilla/5.0'}
)

with urllib.request.urlopen(req) as response:
    page = response.read()

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

episodes = soup.find('table', attrs={'class': 'EpisodeList'})

for row in episodes.children:
    print(row)
    # if row.name == 'tr':
    #     for cell in row.children:
    #         if cell.name == 'td':
    #             print(cell.text)

# Temporarily write the html to a file
# text_file = open("episodes.txt", "w")
# n = text_file.write(str(episodes.contents))
# text_file.close()
