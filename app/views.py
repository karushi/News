from flask import render_template
from app import app
from .request import get_sources
#import get_source

# Views


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # getting general source
    general_sources = get_sources('general')

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title=title, general=general_sources)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html', id=news_id)
