
import unittest
from app.models import Sources
# Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("ars-technica","Ars Technica","The PC enthusiasts resource. Power users and the tools they love, without computing religion.","https://arynews.tv/ud/")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_init(self):
            '''
            test_init to ensure objects are instantiated correctly
            :return:
            '''
            self.assertEqual(self.new_source.id, "ars-technica")
            self.assertEqual(self.new_source.name, "Ars Technica")
            self.assertEqual(self.new_source.description, 'The PC enthusiasts resource. Power users and the tools they love, without computing religion.')
            self.assertEqual(self.new_source.url, "https://arynews.tv/ud/")


# if __name__ == '__main__':
#     unittest.main()