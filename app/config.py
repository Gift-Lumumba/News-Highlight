class Config:
    '''
    General configuration parent class
    '''
    ALL_ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&language=en&sortBy=publishedAt&apiKey={}'
    HEADLINES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&language=en&apiKey={}'
    TECH_NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey={}'
    BUSINESS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&category=business&language=en&apiKey={}'



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