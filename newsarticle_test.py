import unittest
from app.models import Article

class Source(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("BBC NEWS","","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


