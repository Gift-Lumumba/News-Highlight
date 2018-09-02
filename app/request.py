import urllib.request,json
from .models import Source,Article

# Source = source.Source
# Article = article.Article

# Getting api key
api_key = None
base_url = None
business_url = None
sports_url = None
headlines_url = None
technology_url = None
entertainment_url = None
health_url = None
science_url = None

def configure_request(app):
    global api_key,base_url,sports_url,headlines_url,technology_url,entertainment_url,health_url,science_url
    api_key = app.config['ARTICLE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    sports_url = app.config['SPORTS_API_BASE_URL']
    headlines_url = app.config['TOP_HEADLINES_API_BASE_URL']
    technology_url = app.config['TECH_API_BASE_URL']
    entertainment_url = app.config['ENTERTAINMENT_API_BASE_URL']
    health_url = app.config['HEALTH_API_BASE_URL']
    science_url = app.config['SCIENCE_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    Takes news article category as an argument
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        if url:
            source_object = Source(id,name,description,url,category,language)
            source_results.append(source_object)

    return source_results

def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            language = source_details_response.get('language')

            source_object = Source(id,name,description,url,category,language)

    return source_object



def get_articles(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = headlines_url.format(sources,api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        article_results = None

        if get_headlines_response['articles']:
            article_results_list = get_headlines_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if url:
            article_object = Article(author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results

def get_article(id):
    '''
    Function that gets json response from url
    '''
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            author = article_details_response.get('author')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')

            article_object = Article(id,author,description,url,urlToImage,publishedAt)

    return article_object

def get_sports(country):
    '''
    Function that gets the json response to our url request
    '''
    get_sports_url = sports_url.format(country,api_key)

    with urllib.request.urlopen(get_sports_url) as url:
        get_sports_data = url.read()
        get_sports_response = json.loads(get_sports_data)

        sport_results = None

        if get_sports_response['articles']:
            sport_results_list = get_sports_response['articles']
            sport_results = process_results(sport_results_list)


    return sport_results


def get_business(country):
    '''
    Function that gets the json response to our url request
    '''
    get_business_url = business_url.format(country,api_key)

    with urllib.request.urlopen(get_business_url) as url:
        get_business_data = url.read()
        get_business_response = json.loads(get_business_data)

        business_results = None

        if get_business_response['articles']:
            business_results_list = get_business_response['articles']
            business_results = process_results(business_results_list)


    return business_results

def get_technology(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_technology_url = technology_url.format(sources,api_key)

    with urllib.request.urlopen(get_technology_url) as url:
        get_technology_data = url.read()
        get_technology_response = json.loads(get_technology_data)

        technology_results = None

        if get_technology_response['articles']:
            technology_results_list = get_technology_response['articles']
            technology_results = process_results(technology_results_list)


    return technology_results

def get_entertainment(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_entertainment_url = entertainment_url.format(sources,api_key)

    with urllib.request.urlopen(get_entertainment_url) as url:
        get_entertainment_data = url.read()
        get_entertainment_response = json.loads(get_entertainment_data)

        entertainment_results = None

        if get_entertainment_response['articles']:
            entertainment_results_list = get_entertainment_response['articles']
            entertainment_results = process_results(entertainment_results_list)


    return entertainment_results

def get_health(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_health_url = health_url.format(sources,api_key)

    with urllib.request.urlopen(get_health_url) as url:
        get_health_data = url.read()
        get_health_response = json.loads(get_health_data)

        health_results = None

        if get_health_response['articles']:
            health_results_list = get_health_response['articles']
            health_results = process_results(health_results_list)


    return health_results

def get_science(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_science_url = science_url.format(sources,api_key)

    with urllib.request.urlopen(get_science_url) as url:
        get_science_data = url.read()
        get_science_response = json.loads(get_science_data)

        science_results = None

        if get_science_response['articles']:
            science_results_list = get_science_response['articles']
            science_results = process_results(science_results_list)


    return science_results

