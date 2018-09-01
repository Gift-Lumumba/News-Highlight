class Config:
    '''
    General configuration parent class
    '''
    # SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    # EVERYTHING_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    TOP_HEADLINES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SPORTS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category=sports&country={}&apiKey={}'
   



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