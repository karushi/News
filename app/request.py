from app import app
import urllib.request
import json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category, api_key)
    with urllib. request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_responce = json.loads(get_sources_data.decode('utf-8'))

        sources_results = None

        if get_sources_responce['sources']:
            source_results_list = get_sources_responce['sources']
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
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('original_namecategory')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')
        category = source_item.get('category')

        if url:
            source_object = News(id, name, description, url, category, language, country)
            source_results.append(source_object)


        return source_results
