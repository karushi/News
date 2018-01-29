from app import app
import urllib.request
import json
from .models import news

News = news.News

# Getting api key
api_key = app.config['45e91ce609c347dfa903f822aac08388']


# Getting the news base url
base_url = app.conifg['https://newsapi.org/v2/sources?category={}&apiKey={}']
def get_news(category)
