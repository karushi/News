from app import app
import urllib.request
import json
from .models import news, articles

News = news.News
Article = articles.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']
article_url = app.config['ARTICLE_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category, api_key)
    with urllib. request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data.decode('utf-8'))

        sources_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            sources_results = process_results(source_results_list)

        return sources_results


def process_results(sources_list):
    '''
    Function  that processes the source result and transform them to a list of
    Objects

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
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')
        category = source_item.get('category')

        if url:
            source_object = News(id, name, description, url, category,
                                 language, country)
            source_results.append(source_object)

    return source_results


def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_news_url = article_url.format(id, api_key)
    with urllib.request.urlopen(get_article_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data.decode('utf-8'))

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results


def process_articles(articles_list):
    '''
    process the dictionary and output a list of objects
    '''
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            print (id)
            article_object = Article(id, name, author, title, description, url,
                                     urlToImage, publishedAt)

            article_results.append(article_object)

    return article_results
