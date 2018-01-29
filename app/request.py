from app import app
import urllib.request
import json
from .models import news

Movie = news.News

# Getting api key
api_key = app.config['45e91ce609c347dfa903f822aac08388']
