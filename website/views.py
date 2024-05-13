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


url = 'https://www.empireonline.com/movies/features/best-movies-2/'
page = requests.get(url)
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
