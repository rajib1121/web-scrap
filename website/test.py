from bs4 import BeautifulSoup
import requests


url = 'https://www.empireonline.com/movies/features/best-movies-2/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

movie_titles = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

titles = []
rank = [n+1 for n in range(len(movie_titles))]
# rank.insert(0,'Rank')
fields = ['Rank', 'Title']

for title in movie_titles[::-1]:
    # titles.append(title.text)
    x = title.text.split(' ', 1)
    titles.append(x[1])
    # print(x[1])
    # print(title.getText())


new_dict = {
    'Rank' : rank,
    'Title' : titles
}

import pandas as pd
import tkinter as tk
from tkinter import filedialog

df = pd.DataFrame.from_dict(new_dict)

file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("csv file", ".csv")],
                                            )  
if file_path == '':
    print('Please go back and give a file name.')
else:
    df.to_csv(file_path, index = False)

# df.to_csv('list.csv', index=None)