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
        self.new_article = Article("Dakin Andone and Keith Allen, CNN", "There was no sign that children lived in the Hart family home, report says", "In the days after the Hart family's SUV was discovered at the bottom of a California cliff, investigators visited their Washington state home and found almost no evidence that six children lived in the house.","http://us.cnn.com/2018/08/30/us/hart-family-investigation-documents/index.html","https://cdn.cnn.com/cnnnext/dam/assets/180328212418-hart-family-super-tease.jpg","2018-08-31T02:23:02.8234989Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()