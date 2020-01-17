# created by me

from django.shortcuts import render

import requests
requests.packages.urllib3.disable_warnings()
news_list = []
params = {}
from bs4 import BeautifulSoup

def scrape():
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    url = 'https://www.sciencedaily.com/news/computers_math/computer_science/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")
    
    posts = soup.find_all('h3', {'class':'latest-head'})   

    for i in posts:
    	news = i.find('a')
    	news_list.append(news.text)
    	
    params = {'my_news':news_list}
    return params

params = scrape()

def index(request):
    return render(request, 'index.html', params)