from app import app
import urllib.request
import json
from .models import news

News = news.News

# Getting api key
api_key = app.config['45e91ce609c347dfa903f822aac08388']


# Getting the news base url
base_url = app.conifg['https://newsapi.org/v2/sources?category={}&apiKey={}']


def get_sources(category):

    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category, api_key)
    with urllib. request.urlopen(get_source_url)as url:
    get_sources_responce = json.loads(get_sources_data)

    sources_results = None
if get_sources_responce['results']:
    sources_results_list = get_sources_responce['results']
