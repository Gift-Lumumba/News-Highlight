import unittest
from app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Charles Riley","Dyson's electric car plans are taking shape", "The maker of vacuums and hand dryers unveiled plans for 10 miles of test tracks and office space for 2,000 workers at a former RAF training center in England.","https://money.cnn.com/2018/08/30/technology/dyson-electric-car/index.html","https://i2.cdn.turner.com/money/dam/assets/180830115003-dyson-test-track-780x439.jpg","2018-08-30T12:05:22Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()