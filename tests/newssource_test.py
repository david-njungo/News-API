import unittest
from models import Source

class Source(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("bbc-news","BBC NEWS","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","business")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

