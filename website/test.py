from bs4 import BeautifulSoup
import requests
import pandas as pd


# url = "https://edition.cnn.com"

# page = requests.get(url)

# soup = BeautifulSoup(page.content, 'html.parser')

# contents = soup.find_all('a', class_='container__link--type-article', href=True)

# articles = []
# for content in contents:
#     col_headline = content.find_all('span', class_= "container__headline-text")
#     if len(col_headline) == 1:
#         for x in col_headline:
#             links = content['href']
#             text = x.text
#             new_dict = {
#                 'text': text,
#                 'link' : links
#             }
#             articles.append(new_dict)


# for x in articles[5:15]:
#     print (x['text'])



# url = 'https://edition.cnn.com/2024/05/15/china/putin-xi-meeting-china-intl-hnk/index.html'
url = 'https://edition.cnn.com/2024/05/15/politics/mitt-romney-pardon-trump-biden/index.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.h1['class'])

headline = soup.find('h1', class_='headline__text').text.strip()
author = soup.find('div', class_='byline__names').text.strip()
pub_time = soup.find('div', class_='timestamp').string.strip()
body = soup.find('div', class_='article__content').text.strip()
print(body)