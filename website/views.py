from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create your views here.

def home(request):
    return render(request, 'website/index.html', {

    })


movie_url = 'https://www.empireonline.com/movies/features/best-movies-2/'
page = requests.get(movie_url)
soup = BeautifulSoup(page.text, 'html.parser')
movie_titles = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

def movies(request):
    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'html.parser')
    # movie_titles = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')
    title_list = []
        
    for title in movie_titles[:-11:-1]:
        txt = title.text.split(' ', 1)
        title_list.append(txt[1])
    
    return render(request, 'website/movies.html', {
        'data': title_list,
    })


def save_as(request):
    titles = []
    rank = [n+1 for n in range(len(movie_titles))]
    # rank.insert(0,'Rank')
    # fields = ['Rank', 'Title']

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

    df = pd.DataFrame.from_dict(new_dict)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename.csv'

    # df.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    df.to_csv(path_or_buf=response, index=False)
    return response



url = "https://edition.cnn.com"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

articles = []


def news(request):
    contents = soup.find_all('a', class_='container__link--type-article', href=True)
    index_id = 0
    # articles = []
    for content in contents:
        col_headline = content.find_all('span', class_= "container__headline-text")
        if len(col_headline) == 1:
            for x in col_headline:
                # links = url + content['href']
                links = content['href']
                text = x.text
                # new_list = [text, links]
                new_dict = {
                'id' : index_id,
                'text': text,
                'link' : links
            }
                articles.append(new_dict)
                index_id += 1
    return render(request, "website/news.html", {
        'data' : articles[8:18],
    })

def article(request, id):
    index_id = id
    news = articles[id]
    base_url = 'https://edition.cnn.com'
    ref_link = base_url + news['link']
    page = requests.get(ref_link)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.h1['class'])

    headline = soup.find('h1', class_='headline__text').text.strip()
    author = soup.find('div', class_='byline__names').text.strip()
    pub_time = soup.find('div', class_='timestamp').string.strip()
    body = soup.find('div', class_='article__content').text.strip()
    
    data = {
        'headline': headline,
        'author': author,
        'pub': pub_time,
        'body': body,
    }

    return render(request, 'website/article.html', context = data)

    

