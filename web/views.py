# created by me

from django.shortcuts import render

import requests
requests.packages.urllib3.disable_warnings()
params = {}
from bs4 import BeautifulSoup

def scrape():
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    url = 'https://www.sciencedaily.com/news/computers_math/computer_science/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")
    
    posts = soup.find_all('h3', {'class':'latest-head'})   

    labels = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree','twentyfour','twentyfive','twentysix','twentyseven','twentyeight','twentynine','thirty','thirtyone','thirtytwo','thirtythree','thirtyfour']
    j =0
    for i in posts:
    	news = i.find('a')
    	params.update({labels[j]: news.text})
    	j+=1
    	#print(news.text)

scrape()

def index(request):
    return render(request, 'index.html', params)