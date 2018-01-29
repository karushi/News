import unittest
from .models import movie
    News = news.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_News = News("abc_news", "ABC News" "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",  "http://abcnews.go.com", "general",  "en", "us")
