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
    get_source_url = base_url.format(category, api_key)
    with urllib. request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_responce = json.loads(get_sources_data)

        sources_results = None

        if get_sources_responce['sources']:
            source_results_list = get_sources_responce['results']
            sources_results = process_results(source_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of source objects

    Return:
           source_results: A list of source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = News(id, name, "description, url, category, language, country)

    return source_results
