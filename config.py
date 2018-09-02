import os

class Config:
    '''
    General configuration parent class
    '''
    # SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    # EVERYTHING_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    TOP_HEADLINES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SPORTS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category=sports&country={}&apiKey={}'
    BUSINESS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category=business&country={}&apiKey={}'
    TECH_API_BASE_URL = 'https://newsapi.org/v2/everything?q=technology&sources={}&language=en&apiKey={}'
    ENTERTAINMENT_API_BASE_URL = 'https://newsapi.org/v2/everything?q=entertainment&sources={}&language=en&apiKey={}'
    HEALTH_API_BASE_URL = 'https://newsapi.org/v2/everything?q=health&sources={}&language=en&apiKey={}'
    SCIENCE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=science&sources={}&language=en&apiKey={}'


    ARTICLE_API_KEY = os.environ.get('ARTICLE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
   



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}